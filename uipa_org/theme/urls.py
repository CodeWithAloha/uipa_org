from django.urls import re_path, path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps import views as sitemaps_views
from django.contrib.flatpages.views import flatpage
from django.utils.translation import gettext

from froide.urls import (
    admin_urls,
    api_urlpatterns,
    froide_urlpatterns,
    jurisdiction_urls,
    sitemaps,
)

from .views import index

help_url_part = gettext('help')

subpages = [
    'about',
    'faq',
    'privacy',
    'terms',
]

sitemap_urlpatterns = [
    path(
        "sitemap.xml",
        sitemaps_views.index,
        {"sitemaps": sitemaps, "sitemap_url_name": "sitemaps"},
    ),
    path(
        "sitemap-<slug:section>.xml",
        sitemaps_views.sitemap,
        {"sitemaps": sitemaps},
        name="sitemaps",
    ),
]

urlpatterns = []

for subpage in subpages:
    page = '/%s/%s/' % (help_url_part, subpage)
    urlpatterns.append(
        re_path(r'^%s/%s/$' % (help_url_part, subpage), flatpage, {'url': page}, name='%s-%s' % (help_url_part, subpage))
    )
    
urlpatterns += api_urlpatterns
urlpatterns += sitemap_urlpatterns

urlpatterns += i18n_patterns(
    *froide_urlpatterns,
    *jurisdiction_urls,
    *admin_urls,
    prefix_default_language=False
)

urlpatterns += [
    # TODO: Remove this when we have a proper about/help page
    # Redirect /help and /about to /help/faq
    re_path(r'^%s/$' % gettext('help'), flatpage, {'url': '/help/faq/'}, name='help'),
    re_path(r'^%s/$' % gettext('about'), flatpage, {'url': '/help/faq/'}, name='about'),
    # Base case: Redirect all other requests to the index view
    re_path('', index, name='index'),
]
