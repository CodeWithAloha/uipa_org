#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016 Ryan Kanno <ryankanno@localkinegrinds.com>
#
# Distributed under terms of the MIT license.


from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils import translation
from django.utils.translation import override, ugettext, ugettext_lazy as _
from froide.foirequest.models import DeferredMessage
from froide.foirequest.models import FoiRequest
from uipa_org.celery import app as celery_app
from datetime import timedelta


logger = get_task_logger(__name__)

DEFAULT_NOTIFICATION_SENT_BEFORE_NUM_DAYS = 14
DEFAULT_NUM_DAYS_TO_MAKE_PUBLIC_AFTER_DUE_DATE = 365


@celery_app.task
def private_public_reminder(*args, **kwargs):
    translation.activate(settings.LANGUAGE_CODE)

    num_days_after_due_date = settings.FROIDE_CONFIG.get('make_public_num_days_after_due_date', DEFAULT_NUM_DAYS_TO_MAKE_PUBLIC_AFTER_DUE_DATE)
    num_days_after_due_date = num_days_after_due_date - DEFAULT_NOTIFICATION_SENT_BEFORE_NUM_DAYS

    now = timezone.now()
    due_date_everything_should_be_made_private = now - timedelta(num_days_after_due_date)

    logger.info("Attempting to warn all requests that were due on : {0}".format(due_date_everything_should_be_made_private.date()))

    for foirequest in FoiRequest.objects.filter(Q(visibility=0) | Q(visibility=1), is_foi=True, due_date__date=due_date_everything_should_be_made_private.date()):

        logger.info("Sending private/public reminder to request {0} on {1}".format(foirequest.pk, now))

        try:
            send_mail('{0}'.format(
                    _("%(site_name)s: Reminder that your request is being made public in 14 days") % {
                        "site_name": settings.SITE_NAME
                    },
                ),
                render_to_string("foirequest/emails/became_public.txt", {
                    "site_name": settings.SITE_NAME,
                    "request": foirequest,
                }),
                settings.DEFAULT_FROM_EMAIL,
                [foirequest.user.email]
            )
        except Exception as e:
            logger.error(e)


@celery_app.task
def make_private_public(*args, **kwargs):
    translation.activate(settings.LANGUAGE_CODE)
    num_days_after_due_date = settings.FROIDE_CONFIG.get('make_public_num_days_after_due_date', DEFAULT_NUM_DAYS_TO_MAKE_PUBLIC_AFTER_DUE_DATE)
    now = timezone.now()
    due_date_everything_should_be_made_private = now - timedelta(num_days_after_due_date)

    logger.info("Switching all private requests that were due on {0} to public requests.".format(due_date_everything_should_be_made_private))

    for foirequest in FoiRequest.objects.filter(Q(visibility=0) | Q(visibility=1), is_foi=True, due_date__lte=due_date_everything_should_be_made_private):

        logger.info("Switching private foirequest {0} to be made public on {1}".format(foirequest.pk, now))

        foirequest.make_public()

        for message in foirequest.messages:
            for attachment in message.attachments:
                if attachment.can_approve:
                    logger.info("Switching attachment {0} to approved".format(attachment.pk))
                    attachment.approve_and_save()


@celery_app.task
def deferred_message_notification(*args, **kwargs):
    translation.activate(settings.LANGUAGE_CODE)

    today_date = timezone.now().date()
    yesterday_date = today_date + timezone.timedelta(days=-1)

    logger.info("Running notification service for deferred messages on {0}".format(today_date))

    total_deferred_messages = DeferredMessage.objects.count()
    total_deferred_messages_today = DeferredMessage.objects.filter(timestamp__date=today_date).count()
    total_deferred_messages_yesterday = DeferredMessage.objects.filter(timestamp__date=yesterday_date).count()

    if (total_deferred_messages_today > 0) or (total_deferred_messages_yesterday > 0):

        logger.info("Deferred messages came in yesterday / today -> sending notification email")

        try:
            send_mail('{0}'.format(
                    _("%(site_name)s: You have deferred messages from yesterday/today") % {
                        "site_name": settings.SITE_NAME
                    },
                ),
                render_to_string("foirequest/emails/admin_deferred_message_notifications.txt", {
                    "site_name": settings.SITE_NAME,
                    "today_date": today_date,
                    "total_deferred_messages": total_deferred_messages,
                    "total_deferred_messages_yesterday": total_deferred_messages_yesterday,
                    "total_deferred_messages_today": total_deferred_messages_today,
                }),
                settings.DEFAULT_FROM_EMAIL,
                [a[1] for a in settings.ADMINS]
            )
        except Exception as e:
            logger.error(e)
