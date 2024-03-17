# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base import UipaOrgThemeBase, env

class Dev(UipaOrgThemeBase):
    DEBUG = True

    CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}
