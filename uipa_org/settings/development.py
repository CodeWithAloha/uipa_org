# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base import UipaOrgThemeBase, env

class Dev(UipaOrgThemeBase):
    DEBUG = True

    # Don't use the Vite server for frontend assets.
    # Prerequisite: Run `yarn build` to create the assets in the build directory.
    FRONTEND_DEBUG = False

    CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}

    @property
    def TEMPLATES(self):
        TEMP = super().TEMPLATES
        TEMP[0]["OPTIONS"]["debug"] = True
        return TEMP
