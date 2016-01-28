# -*- coding: utf-8 -*-
from configurations import values
from froide.settings import Base
from froide.settings import ThemeBase
from froide.settings import os_env
import os
import re


rec = lambda x: re.compile(x, re.I | re.U)


class UipaOrgThemeBase(ThemeBase):
    FROIDE_THEME = 'uipa_org.theme'

    SITE_NAME = "UIPA"
    SITE_EMAIL = "info@example.com"
    SITE_URL = 'http://localhost:8000'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, "..", "public"))

    FIXTURE_DIRS = ('fixtures',)

    @property
    def INSTALLED_APPS(self):
        installed = super(UipaOrgThemeBase, self).INSTALLED_APPS
        installed += [
            'celery_haystack',
            'djcelery_email',
            'django.contrib.redirects',
            'tinymce'
        ]
        return installed

    MIDDLEWARE_CLASSES = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
        'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
        'froide.account.middleware.AcceptNewTermsMiddleware',
    ]

    TINYMCE_DEFAULT_CONFIG = {
        'plugins': "table,spellchecker,paste,searchreplace",
        'theme': "advanced",
        'cleanup_on_startup': False
    }

    SECRET_URLS = values.DictValue({
        "admin": "uipa-admin",
        "postmark_inbound": "uipa_postmark_inbound",
        "postmark_bounce": "uipa_postmark_bounce"
    })

    @property
    def FROIDE_CONFIG(self):
        config = super(UipaOrgThemeBase, self).FROIDE_CONFIG
        config.update(dict(
            create_new_publicbody=True,
            publicbody_empty=True,
            user_can_hide_web=True,
            public_body_officials_public=True,
            public_body_officials_email_public=False,
            request_public_after_due_days=14,
            payment_possible=False,
            default_law=1,
            greetings=[rec(u"Dear (?:Mr\.?|Ms\.? .*?)")],
            closings=[rec(u"Sincerely yours,?")],
            public_body_boosts={},
            dryrun=False,
            dryrun_domain="beta.uipa.org",
            allow_pseudonym=False,
            doc_conversion_binary=None,  # replace with libreoffice instance
            doc_conversion_call_func=None,  # see settings_test for use
            api_activated=True,
            search_engine_query='http://www.google.com/search?as_q=%(query)s&as_epq=&as_oq=&as_eq=&hl=en&lr=&cr=&as_ft=i&as_filetype=&as_qdr=all&as_occt=any&as_dt=i&as_sitesearch=%(domain)s&as_rights=&safe=images',
            show_public_body_employee_name=False
        ))
        return config


class Dev(UipaOrgThemeBase, Base):
    CACHES = {
        'default': {
            'LOCATION': 'dev-uipa',
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
        }
    }


class Beta(UipaOrgThemeBase, Base):
    SITE_URL = values.Value('http://beta.uipa.org')
    SITE_EMAIL = 'info@beta.uipa.org'
    DEFAULT_FROM_EMAIL = 'info@beta.uipa.org'

    CACHES = {
        'default': {
            'LOCATION': 'beta-uipa',
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
        }
    }

    HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'

    ALLOWED_HOSTS = values.TupleValue(('beta.uipa.org',))

    FOI_EMAIL_TEMPLATE = values.Value('request+{secret}@{domain}')
    FOI_EMAIL_DOMAIN = values.Value('beta.uipa.org')

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    SERVER_EMAIL = values.Value(os_env('POSTMARK_INBOUND_ADDRESS'))
    DEFAULT_FROM_EMAIL = values.Value(os_env('POSTMARK_INBOUND_ADDRESS'))

    DATABASES = values.DatabaseURLValue(os_env('DATABASES'))
    BROKER_URL = os_env('BROKER_URL')
    CELERY_RESULT_BACKEND = os_env('CELERY_RESULT_BACKEND')

    # Official Notification Mail goes through
    # the normal Django SMTP Backend
    EMAIL_HOST = os_env('POSTMARK_SMTP_SERVER')
    EMAIL_PORT = values.IntegerValue(2525)
    EMAIL_HOST_USER = os_env('POSTMARK_API_KEY')
    EMAIL_HOST_PASSWORD = os_env('POSTMARK_API_KEY')
    EMAIL_USE_TLS = values.BooleanValue(True)

    # SMTP settings for sending FoI mail
    FOI_EMAIL_FIXED_FROM_ADDRESS = values.BooleanValue(False)
    FOI_EMAIL_HOST_FROM = os_env('POSTMARK_INBOUND_ADDRESS')
    FOI_EMAIL_HOST_USER = os_env('POSTMARK_API_KEY')
    FOI_EMAIL_HOST_PASSWORD = os_env('POSTMARK_API_KEY')
    FOI_EMAIL_HOST = os_env('POSTMARK_SMTP_SERVER')
    FOI_EMAIL_PORT = values.IntegerValue(2525)
    FOI_EMAIL_USE_TLS = values.BooleanValue(True)


class Production(UipaOrgThemeBase, Base):
    DEBUG = False
    TEMPLATE_DEBUG = False

    CELERY_ALWAYS_EAGER = values.BooleanValue(False)
    COMPRESS_ENABLED = values.BooleanValue(True)
    COMPRESS_OFFLINE = values.BooleanValue(True)

    SITE_URL = values.Value('http://uipa.org')
    SITE_EMAIL = 'info@uipa.org'
    DEFAULT_FROM_EMAIL = 'info@uipa.org'

    CACHES = {
        'default': {
            'LOCATION': 'production-uipa',
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
        }
    }

    ALLOWED_HOSTS = values.TupleValue(('uipa.org',))

    FOI_EMAIL_TEMPLATE = values.Value('request+{secret}@{domain}')
    FOI_EMAIL_DOMAIN = values.Value('beta.uipa.org')

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    SERVER_EMAIL = values.Value(os_env('POSTMARK_INBOUND_ADDRESS'))
    DEFAULT_FROM_EMAIL = values.Value(os_env('POSTMARK_INBOUND_ADDRESS'))

    DATABASES = values.DatabaseURLValue(os_env('DATABASES'))
    BROKER_URL = os_env('BROKER_URL')
    CELERY_RESULT_BACKEND = os_env('CELERY_RESULT_BACKEND')

    # Official Notification Mail goes through
    # the normal Django SMTP Backend
    EMAIL_HOST = os_env('POSTMARK_SMTP_SERVER')
    EMAIL_PORT = values.IntegerValue(2525)
    EMAIL_HOST_USER = os_env('POSTMARK_API_KEY')
    EMAIL_HOST_PASSWORD = os_env('POSTMARK_API_KEY')
    EMAIL_USE_TLS = values.BooleanValue(True)

    # SMTP settings for sending FoI mail
    FOI_EMAIL_FIXED_FROM_ADDRESS = values.BooleanValue(False)
    FOI_EMAIL_HOST_FROM = os_env('POSTMARK_INBOUND_ADDRESS')
    FOI_EMAIL_HOST_USER = os_env('POSTMARK_API_KEY')
    FOI_EMAIL_HOST_PASSWORD = os_env('POSTMARK_API_KEY')
    FOI_EMAIL_HOST = os_env('POSTMARK_SMTP_SERVER')
    FOI_EMAIL_PORT = values.IntegerValue(2525)
    FOI_EMAIL_USE_TLS = values.BooleanValue(True)

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
