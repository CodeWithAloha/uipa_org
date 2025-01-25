

# This should have been added to supervisord
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uipa_org.settings')
# os.environ.setdefault("DJANGO_CONFIGURATION", "Beta")

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uipa_org.settings')
os.environ.setdefault("DJANGO_CONFIGURATION", "Beta")

from celery import Celery
from django.conf import settings

import configurations
configurations.setup()

app = Celery('uipa_org')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, related_name='tasks')
