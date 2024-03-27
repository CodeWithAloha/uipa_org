# -*- coding: utf-8 -*-
from __future__ import absolute_import

from configurations import values
from froide.settings import Base
import os
import re
from pathlib import Path

rec = lambda x: re.compile(x, re.I | re.U)

def env(key, default=None):
    return os.environ.get(key, default)

THEME_ROOT = Path(__file__).resolve().parent.parent

# Note: The settings in this file are either Django settings or Froide settings.
# Django settings are documented at https://docs.djangoproject.com/en/4.2/ref/settings/ (or the version of Django you are using).
# Froide settings are documented at https://froide.readthedocs.io/en/latest/configuration/

class UipaOrgThemeBase(Base):
    FROIDE_THEME = 'uipa_org.theme'
    ROOT_URLCONF = "uipa_org.theme.urls"

    SITE_NAME = "UIPA.org"
    SITE_EMAIL = "info@uipa.org"
    SITE_URL = 'http://localhost:8000'
    
    FRONTEND_BUILD_DIR = THEME_ROOT.parent / "build"
    STATIC_ROOT = values.Value(THEME_ROOT.parent / "public")
    
    FIXTURE_DIRS = ('fixtures',)

    @property
    def STATICFILES_DIRS(self):
        return [THEME_ROOT / "theme/static"] + super().STATICFILES_DIRS
    
    @property
    def TEMPLATES(self):
        TEMP = super().TEMPLATES
        if "DIRS" not in TEMP[0]:
            TEMP[0]["DIRS"] = []
        TEMP[0]["DIRS"] = [
            THEME_ROOT / "templates",
        ] + list(TEMP[0]["DIRS"])
        cps = TEMP[0]["OPTIONS"]["context_processors"]
        cps.extend(
            [
                # "sekizai.context_processors.sekizai",
                # "cms.context_processors.cms_settings",
            ]
        )
        return TEMP

    @property
    def INSTALLED_APPS(self):
        installed = super(UipaOrgThemeBase, self).INSTALLED_APPS
        installed = (
            installed.default + 
            [
                "django.contrib.postgres",
                "django.db.backends.postgresql",
                "django.contrib.redirects",
                'floppyforms',
                'uipa_org.uipa_constants',
                'uipa_org.theme.templatetags.uipa_extras',
            ]
        )
        return installed
    
    MIDDLEWARE = [
        "django.middleware.locale.LocaleMiddleware",  # needs to be before CommonMiddleware
        "django.middleware.common.CommonMiddleware",
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    ]

    # https://froide.readthedocs.io/en/latest/configuration/
    # https://github.com/okfde/froide/blob/d9baeae8fc399d524d931dc96d56ca31d5abc094/froide/settings.py#L516
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
            greetings=[rec(u"Aloha (?:Mr\.?|Ms\.? .*?)")],
            closings=[rec(u"Mahalo,?")],
            public_body_boosts={},
            dryrun=False,
            dryrun_domain="test.uipa.org",
            allow_pseudonym=False,
            doc_conversion_binary="/Applications/LibreOffice.app/Contents/MacOS/soffice",
            doc_conversion_call_func=None,  # see settings_test for use
            api_activated=True,
            search_engine_query='http://www.google.com/search?as_q=%(query)s&as_epq=&as_oq=&as_eq=&hl=en&lr=&cr=&as_ft=i&as_filetype=&as_qdr=all&as_occt=any&as_dt=i&as_sitesearch=%(domain)s&as_rights=&safe=images',
            show_public_body_employee_name=False,
        ))
        return config
