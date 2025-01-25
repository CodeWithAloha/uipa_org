# -*- coding: utf-8 -*-


from celery.schedules import crontab
from configurations import values
from froide.settings import Base
from froide.settings import ThemeBase
from froide.settings import os_env
import os
import re


rec = lambda x: re.compile(x, re.I | re.U)


class UipaOrgThemeBase(ThemeBase):
    FROIDE_THEME = 'uipa_org.theme'

    SITE_NAME = "UIPA.org"
    SITE_EMAIL = "info@example.com"
    SITE_URL = 'http://localhost:8000'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, "..", "public"))

    FIXTURE_DIRS = ('fixtures',)

    MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

    SECRET_KEY = os_env('SECRET_KEY')

    MEDIA_ROOT = os_env('MEDIA_ROOT')

    DATA_UPLOAD_MAX_MEMORY_SIZE = 26214400  # 25MB

    TAGGING_AUTOCOMPLETE_MAX_TAGS = 100

    @property
    def INSTALLED_APPS(self):
        installed = super(UipaOrgThemeBase, self).INSTALLED_APPS
        installed += [
            'celery_haystack',
            'djcelery_email',
            'django.contrib.redirects',
            'uipa_org.uipa_constants',
            'uipa_org.theme.templatetags.uipa_extras',
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

    HAYSTACK_CONNECTIONS = {
        'default': {
            #'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'haystack',
            #'KWARGS': {
            #        'http_auth': ('elastic', 'froide'),
            #},
        }
    }

    TIME_ZONE = values.Value('Pacific/Honolulu')

    CELERY_IMPORTS = ('uipa_org.tasks',)
    CELERY_TIMEZONE = values.Value('Pacific/Honolulu')

    CELERYBEAT_SCHEDULE = {
        'fetch-mail': {
            'task': 'froide.foirequest.tasks.fetch_mail',
            'schedule': crontab(),
        },
        'detect-asleep': {
            'task': 'froide.foirequest.tasks.detect_asleep',
            'schedule': crontab(hour=0, minute=0),
        },
        'detect-overdue': {
            'task': 'froide.foirequest.tasks.detect_overdue',
            'schedule': crontab(hour=0, minute=0),
        },
        'update-foirequestfollowers': {
            'task': 'froide.foirequestfollower.tasks.batch_update',
            'schedule': crontab(hour=0, minute=0),
        },
        'classification-reminder': {
            'task': 'froide.foirequest.tasks.classification_reminder',
            'schedule': crontab(hour=7, minute=0, day_of_week=6),
        },
        'uipa-private_public_reminder': {
            'task': 'uipa_org.tasks.private_public_reminder',
            'schedule': crontab(hour=0, minute=0),
        },
        'uipa-make_public_private': {
            'task': 'uipa_org.tasks.make_private_public',
            'schedule': crontab(hour=0, minute=0),
        },
        'uipa-deferred_message_notification': {
            'task': 'uipa_org.tasks.deferred_message_notification',
            'schedule': crontab(hour=6, minute=0),
        },
    }

    CELERY_RESULT_BACKEND = 'rpc'
    CELERY_RESULT_PERSISTENT = True

    @property
    def FROIDE_CONFIG(self):
        config = super(UipaOrgThemeBase, self).FROIDE_CONFIG
        config.update(dict(
            currency="Dollars",
            create_new_publicbody=False,
            publicbody_empty=False,
            user_can_hide_web=True,
            public_body_officials_public=True,
            public_body_officials_email_public=False,
            request_public_after_due_days=14,
            payment_possible=False,
            default_law=1,
            greetings=[rec("Aloha (?:Mr\.?|Ms\.? .*?)")],
            closings=[rec("Mahalo,?")],
            public_body_boosts={},
            dryrun=True,
            dryrun_domain="beta.uipa.org",
            allow_pseudonym=False,
            # doc_conversion_binary=None,  # replace with libreoffice instance
            doc_conversion_binary="/Applications/LibreOffice.app/Contents/MacOS/soffice",
            doc_conversion_call_func=None,  # see settings_test for use
            api_activated=True,
            search_engine_query='http://www.google.com/search?as_q=%(query)s&as_epq=&as_oq=&as_eq=&hl=en&lr=&cr=&as_ft=i&as_filetype=&as_qdr=all&as_occt=any&as_dt=i&as_sitesearch=%(domain)s&as_rights=&safe=images',
            show_public_body_employee_name=False,
            make_public_num_days_after_due_date=365,
            ga_tracking_id=os_env('GA_TRACKING_ID'),
        ))
        return config


class NginxSecureStaticEnabled(object):
    USE_X_ACCEL_REDIRECT = True
    X_ACCEL_REDIRECT_PREFIX = values.Value('/protected')


class SslEnabled(object):
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True


class SentryEnabled(object):
    RAVEN_CONFIG = {
        'dsn': os_env('SENTRY_DSN')
    }


class S3Enabled(object):
    AWS_ACCESS_KEY_ID = os_env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os_env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os_env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_SECURE_URLS = values.Value(True)
    AWS_QUERYSTRING_AUTH = values.Value(False)

    AWS_S3_HOST = 's3-us-west-1.amazonaws.com'
    AWS_S3_CALLING_FORMAT = 'boto.s3.connection.OrdinaryCallingFormat'
    AWS_S3_CUSTOM_DOMAIN = '%s.%s' % (AWS_STORAGE_BUCKET_NAME, AWS_S3_HOST)
    AWS_S3_FILE_OVERWRITE = False

    STATICFILES_STORAGE = values.Value('uipa_org.custom_storages.CachedS3BotoStorage')
    STATICFILES_LOCATION = 'static'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    COMPRESS_STORAGE = values.Value('uipa_org.custom_storages.CachedS3BotoStorage')
    COMPRESS_URL = values.Value(STATIC_URL)

    # @ryankanno - Can't store media files in S3 because of auth issue
    # DEFAULT_FILE_STORAGE = values.Value('uipa_org.custom_storages.MediaStorage')
    # MEDIAFILES_LOCATION = 'media'
    # MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

    AWS_HEADERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }
    AWS_IS_GZIPPED = True

    GZIP_CONTENT_TYPES = (
        'text/css',
        'application/javascript',
        'application/x-javascript',
        'text/javascript'
    )


class Dev(UipaOrgThemeBase, Base):

    DEBUG = True
    ALLOWED_HOSTS = values.TupleValue(('localhost', '127.0.0.1'))

    COMPRESS_ENABLED = values.BooleanValue(True)
    COMPRESS_OFFLINE = True

    STATIC_URL = '/static/'
    COMPRESS_URL = values.Value(STATIC_URL)

    @property
    def COMPRESS_OFFLINE_CONTEXT(self):
        return {
            "DEBUG": super(Dev, self).DEBUG,
            "STATIC_URL": super(Dev, self).STATIC_URL
        }

    # uploads subdirectory in the directory where this settings file lives.
    MEDIA_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploads')

    CACHES = {
        'default': {
            'LOCATION': 'dev-uipa',
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
        }
    }

    SECRET_KEY = 'make_me_unique!!'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'DEBUG',
            'handlers': ['uipa_org_logfile',],
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'formatters': {
            'verbose': {
                'format': '[%(asctime)s] %(levelname)s (pid: %(process)d) [%(name)s.%(module)s: %(funcName)s:%(lineno)d] %(message)s',
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
            },
            'uipa_org_logfile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': 'uipa_org_dev_app.log', # put in the working directory
                'maxBytes': 1024*1024*5,  # 5MB
                'backupCount': 10,
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'froide': {
                'handlers': ['uipa_org_logfile'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'django': {
                'handlers': ['uipa_org_logfile'],
                'level': 'DEBUG',
                'propagate': False,
            },
            # Use instead of 'django.request' to log all requests; added in Django 1.11.
            'django.server': {
                'handlers': ['uipa_org_logfile'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'django.security': {
                'handlers': ['uipa_org_logfile'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'django.db.backends': {
                'level': 'DEBUG',
                'handlers': ['uipa_org_logfile'],
                'propagate': False,
            },
            'django.template': {
                'level': 'INFO',
                'handlers': ['uipa_org_logfile'],
                'propagate': False,
            },
            'uipa_org': {
                'handlers': ['uipa_org_logfile'],
                'level': 'DEBUG',
                'propagate': False,
            },
        }
    }

    HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'

    ## For elasticsearch connection authentication.
    #from urllib.parse import urlparse
    #parsed = urlparse("http://elastic:froide@127.0.0.1:9200")

    HAYSTACK_CONNECTIONS = {
        'default': {
            #'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
            'INDEX_NAME': 'haystack',
            'URL': 'http://127.0.0.1:9200'
            # elasticsearch 2.x doesn't have authentication.
            #'URL': parsed.hostname,
            #'KWARGS': {
            #    'port': parsed.port,
            #    'http_auth': (parsed.username, parsed.password),
            #    'use_ssl': False,
            #},
        }
        #'default': {
        #    # This doesn't support updates.
        #    'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        #}
    }

    DATABASES = {
        'default': {
            #'ENGINE': 'django.db.backends.sqlite3',  # Load from fixtures doesn't work with SQLite3.
            #'NAME': 'dev.db',
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'uipa',
            'USER': 'uipa',
            'PASSWORD': 'uipa',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

    # Send email to the console
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    @property
    def FROIDE_CONFIG(self):
        config = super(Dev, self).FROIDE_CONFIG
        config.update(dict(
            dryrun=False,
            make_public_num_days_after_due_date=365,
            doc_conversion_binary="/Applications/LibreOffice.app/Contents/MacOS/soffice",
        ))
        return config

    TEST_SELENIUM_DRIVER = 'chromedriver'

class Beta(SentryEnabled, NginxSecureStaticEnabled, S3Enabled, SslEnabled, UipaOrgThemeBase, Base):

    COMPRESS_ENABLED = values.BooleanValue(True)
    COMPRESS_OFFLINE = values.BooleanValue(True)

    SITE_URL = values.Value('https://beta.uipa.org')
    SITE_EMAIL = 'info@beta.uipa.org'
    DEFAULT_FROM_EMAIL = 'info@beta.uipa.org'

    ADMINS = [('Admin', 'admin@beta.uipa.org'),]

    CACHES = {
        'default': {
            'LOCATION': 'beta-uipa',
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
        }
    }

    HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'haystack',
        }
    }

    ALLOWED_HOSTS = values.TupleValue(('beta.uipa.org',))

    FOI_EMAIL_TEMPLATE = values.Value('request+{secret}@{domain}')
    FOI_EMAIL_DOMAIN = values.Value('beta-foi.uipa.org')

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

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'DEBUG',
            'handlers': ['uipa_org_logfile',],
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'formatters': {
            'verbose': {
                'format': '[%(asctime)s] %(levelname)s [%(module)s %(process)d %(thread)d - %(name)s.%(funcName)s:%(lineno)d] %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
            },
            'uipa_org_logfile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join('/var/log/uipa_org_beta/', 'uipa_org_beta_app.log'),
                'maxBytes': 1024*1024*5,  # 5MB
                'backupCount': 10,
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'froide': {
                'handlers': ['uipa_org_logfile'],
                'level': 'DEBUG',
            },
            'django': {
                'handlers': ['uipa_org_logfile'],
                'level': 'DEBUG'
            },
            'django.request': {
                'handlers': ['uipa_org_logfile'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'django.security': {
                'handlers': ['uipa_org_logfile'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'django.db.backends': {
                'level': 'DEBUG',
                'handlers': ['uipa_org_logfile'],
                'propagate': False,
            },
            'uipa_org': {
                'handlers': ['uipa_org_logfile'],
                'level': 'DEBUG',
            },
        }
    }

    @property
    def FROIDE_CONFIG(self):
        config = super(Beta, self).FROIDE_CONFIG
        config.update(dict(
            payment_possible=True,
            make_public_num_days_after_due_date=365,
            doc_conversion_binary="/usr/bin/libreoffice"))
        return config


class Production(SentryEnabled, NginxSecureStaticEnabled, S3Enabled, SslEnabled, UipaOrgThemeBase, Base):
    DEBUG = False
    TEMPLATE_DEBUG = False

    COMPRESS_ENABLED = values.BooleanValue(True)
    COMPRESS_OFFLINE = values.BooleanValue(True)

    SITE_URL = values.Value('https://uipa.org')
    SITE_EMAIL = 'info@uipa.org'
    DEFAULT_FROM_EMAIL = 'info@uipa.org'

    ADMINS = [('Admin', 'admin@uipa.org'), ('Ryan', 'ryan@codeforhawaii.org')]

    CACHES = {
        'default': {
            'LOCATION': 'production-uipa',
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
        }
    }

    HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'haystack',
        }
    }

    ALLOWED_HOSTS = values.TupleValue(('uipa.org', 'www.uipa.org'))

    FOI_EMAIL_TEMPLATE = values.Value('request+{secret}@{domain}')
    FOI_EMAIL_DOMAIN = values.Value('foi.uipa.org')

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

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'DEBUG',
            'handlers': ['uipa_org_logfile'],
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'formatters': {
            'verbose': {
                'format': '[%(asctime)s] %(levelname)s [%(module)s %(process)d %(thread)d - %(name)s.%(funcName)s:%(lineno)d] %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
            },
            'uipa_org_logfile': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join('/var/log/uipa_org/', 'uipa_org_app.log'),
                'maxBytes': 1024*1024*5,  # 5MB
                'backupCount': 10,
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'froide': {
                'handlers': ['uipa_org_logfile', 'mail_admins'],
                'level': 'DEBUG',
            },
            'django': {
                'handlers': ['uipa_org_logfile', 'mail_admins'],
                'level': 'ERROR'
            },
            'django.request': {
                'handlers': ['uipa_org_logfile', 'mail_admins'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.security': {
                'handlers': ['uipa_org_logfile', 'mail_admins'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['uipa_org_logfile', 'mail_admins'],
                'propagate': False,
            },
            'uipa_org': {
                'handlers': ['uipa_org_logfile', 'mail_admins'],
                'level': 'DEBUG',
            }
        }
    }

    @property
    def FROIDE_CONFIG(self):
        config = super(Production, self).FROIDE_CONFIG
        config.update(dict(
            payment_possible=True,
            dryrun=False,
            make_public_num_days_after_due_date=365,
            doc_conversion_binary="/usr/bin/libreoffice"))
        return config

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
