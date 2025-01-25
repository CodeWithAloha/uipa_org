# Roadmap to updgrade UIPA to Django 4.2 and Python 3.10

*Last update: 01/11/2025*  

## Status

| Item   | Working Version | Production Version |
| ---    | ---:            | ---: |
| Django | 1.11            | 1.9 |
| Python |  3.8            | 2.7 |

Repo: https://github.com/CodeWithAloha/uipa/tree/master

Froide source merged into UIPA.org in update branch of russtoku's fork of UIPA.org.

### Change Log

- **01/11/2025:** Added site map based on update branch of russtoku fork.
- **12/23/2024:** Fixed some broken things. Removed django-overextends
dependency because the functionality is included in Django 1.9.
- **11/14/2024:** Incorporated froide into uipa project source instead of being
an editable dependency.
- **10/18/2024:** Upgraded to Django 1.11.29 and Python 3.8 (3.7 is the highest
version supported for Django 1.11.29).
- **04/28/2024:** Started.

### Next steps

See the sections below the ROADMAP for more details.

- Finish up **3** (*Upgrade Python to 3.8*) before tackling **8** (*Upgrade Django to
2.0.13*).
- **7** (*Figure out deployment for production*) can be put on hold for a while.


## ROADMAP

  1. Upgrade Django to 1.11.29 (LTS; last version to support Python 2.7)
     with Python 2.7.15.
     - **Completed:** 10/03/2024
        - Can't add public bodies in Admin site.
        - Making a request paritally fails when no elasticsearch or solr.
     - https://docs.djangoproject.com/en/1.11/
     - https://docs.djangoproject.com/en/1.11/releases/1.11/ (Release Notes)

     - New in Django 1.11
       - Class-based model indexes
       - Template-based widget rendering
       - Subquery expressions

     - Backwards incompatible changes in Django 1.11
       - GDAL is a required dependency
       - Dropped support for PostgreSQL 9.2 and PostGIS 2.0
       - pytz is a required dependency
       - get_model() and get_models() now raise AppRegistryNotReady if
         they’re called before models of all applications have been loaded.
         If you need the old behavior of get_model(), set the require_ready
         argument to False.

  2. Upgrade Python to 3.7 (highest supported by Django 1.11.17).
     - **Completed:** 10/08/2024
        - Search is working with elasticsearch and django-haystack (supports
        only up to elasticsearch 2.x).
        - No pysolr/Solr.
        - 2to3 refactorings.

  3. Upgrade Python to 3.8
     - **Mostly Completed:** 10/14/2024
     - Does work with Django 1.11.17.
     - Python 3.8 is no longer supported as of 10/07/2024.
     - Add [site map](uipa-site-map.md). **Completed:** 01/11/2025
     - TODO:
       - Create test plan and tests because there are major changes with Django
         2.0.
         - Use `pytest` instead of Django's "manage.py test" which uses
         `unittest`.
     - **WON'T DO**
       - Install GDAL, postgis, and libgeoip for django-floppyforms or not.
         - Can leave things the way they are without GDAL, postgis, and
           libgeoip because they aren't really being used; especially
           floppyforms GEO widgets.
         - If don't need the GIS stuff, see:
           https://github.com/jazzband/django-floppyforms/issues/189#issuecomment-379546682

  4. Incorporate froide as apps instead of a dependency. (Added 11/1/2024)
     - **Completed:** 11/17/2024
     - This makes it easier to make changes to froide by eliminating the need to
       maintain two repos for the UIPA.org website.

  5. Remove django-overextends dependency because Django 1.9 already provides
     the same capabilities. (Added 11/15/2024)
     - **Completed:** 12/22/2024
     - Remove `overextends` from `INSTALLED_APPS` in `froide/settings.py`.
     - Remove `django-overextends` from `requirements.txt`.
     - Change `overextends` to `extends` in templates under `uipa_org`
       directory.

  6. ~~Set up Postfix in a Docker container.~~ Create local test mail server.
     - **Completed:** 12/22/2024
     - **Created test mail server program:** 10/18/2024; see
      [https://github.com/russtoku/test-mail-server](https://github.com/russtoku/test-mail-server)
     - TODO:
       - Send outgoing from UIPA to it.
       - Pull incoming email to UIPA from it.

  7. Figure out deployment for production.
      - What are the pieces?

  8. Upgrade Django to 2.0.13 (needs Python 3.4+).
     - https://docs.djangoproject.com/en/2.0/releases/2.0/

     - Run with `-Wa` to show deprecations.

     - New in Django 2.0
       - django.urls.path() function allows a simpler, more readable URL
         routing syntax
       - django.conf.urls.url() function from previous versions is now
         available as django.urls.re_path()
       - Mobile-friendly contrib.admin
       - runserver Web server supports HTTP 1.1

     - Backwards incompatible changes in Django 1.11
       - Removed support for bytestrings in some places
         - call `decode()` on the bytestring before passing it to `reverse()`
       - Form fields no longer accept optional arguments as positional
         arguments
       - Indexes no longer accept positional arguments
       - Foreign key constraints are now enabled on SQLite
         - Should fix a problem when loading fixtures.
         - Fixed a schema corruption issue on SQLite 3.26+. You might have
           to drop and rebuild your SQLite database if you applied
           a migration while using an older version of Django with SQLite
           3.26 or later (#29182). [Django 2.0.10]
       - default HTTP error handlers (handler404, etc.) are now callables
         instead of dotted Python path strings

     - Features removed in Django 2.0
       - django.core.urlresolvers module is removed in favor of its new
         location, django.urls
       - Using User.is_authenticated() and User.is_anonymous() as methods
         rather than properties is no longer supported

  9. Upgrade Django to 2.115.

 10. Upgrade Django to 2.2.28 (supports Python 3.9) so we can use
     https://github.com/adamchainz/django-upgrade.

 11. Upgrade Python to 3.9 (highest supported by Django 2.2.17).

 12. Upgrade Django to 3.0.14 (needs Python 3.6+, supports 3.9 as of 3.0.11).
     - ASGI support
     - Model.save() no longer attempts to find a row when saving a new Model
       instance and a default value for the primary key is provided, and
       always performs a single INSERT query
     - Removed private Python 2 compatibility APIs
     - New default value for the FILE_UPLOAD_PERMISSIONS setting
     - New default values for security settings

 13. Upgrade Django to 3.1.14 (needs Python 3.6+, supports 3.9 as of 3.1.3).
     - Asynchronous views and middleware support
     - JSONField for all supported database backends

 14. Upgrade Django to 3.2.25 (needs Python 3.6+, supports 3.10 as of 3.2.9).
     - Automatic AppConfig discovery
     - django.core.paginator.Paginator.get_elided_page_range() method
       allows generating a page range with some of the values elided
     - Response headers are now stored in HttpResponse.headers

 15. Upgrade Python to 3.10 (highest supported by Django 3.2.9).

 16. Upgrade Django to 4.0.10 (needs Python 3.8+)
     - Python standard library’s zoneinfo is now the default timezone
       implementation
     - scrypt password hasher
     - Forms, Formsets, and ErrorList are now rendered using the template
       engine to enhance customization
     - admin/base.html template now has a new block header which contains
       the admin site header
     - ManifestStaticFilesStorage now replaces paths to JavaScript source
       map references with their hashed counterparts
       - Can use ViteJS now?
     - runserver management command now supports the --skip-checks option
     - new stdout argument for pre_migrate() and post_migrate() signals
       allows redirecting output to a stream-like object. It should be
       preferred over sys.stdout and print() when emitting verbose output in
       order to allow proper capture when testing
     - Dropped support for PostgreSQL 9.6

 17. Upgrade Django to 4.1.13 (needs Python 3.8+, support 3.11 as of 4.1.3)
     - Asynchronous handlers for class-based views
     - Asynchronous ORM interface
     - Check, unique, and exclusion constraints defined in the
       Meta.constraints option are now checked during model validation
     - Form rendering accessibility
     - ManifestStaticFilesStorage now replaces paths to CSS source map
       references with their hashed counterparts
     - Dropped support for PostgreSQL 10
     - default_app_config application configuration variable is removed

 18. Upgrade Django to 4.2 (needs Python 3.8+, support 3.12 as of 4.2.8)
     - Psycopg 3 support; psycopg 3 introduces some breaking changes over
       psycopg2
     - Dropped support for PostgreSQL 11
     - to avoid updating unnecessary columns, QuerySet.update_or_create()
       now passes update_fields to the Model.save() calls
     - undocumented django.http.multipartparser.parse_header() function is
       removed. Use django.utils.http.parse_header_parameters() instead

 19. Upgrade Python to 3.12 (highest supported by Django 4.2.8).


## What is this about?

The [Public First Law Center](https://www.publicfirstlaw.org/) (formerly Civil
Beat Law Center) wants to get UIPA.org on modern, supported versions of Python
and Django.

The site went live on September 2018 using Python 2.7 and Django 1.9. Both are
have been unsupported for a long time. See the Repositories section below for
the versions of Froide and Froide Theme.

Currently, Code With Aloha is pursuing an
[upgrade](https://github.com/orgs/CodeWithAloha/projects/14) of
[UIPA.org](https://github.com/CodeWithAloha/uipa/wiki) using the latest version
of Froide using Python 3.10 and Django 4.2.

This roadmap is an alternate approach to upgrading UIPA.org to Python 3.10 and
Django 4.2. The newer version of Froide has more feaures that the old
version. The additional features are not likely to be used by UIPA.org
users. Additionally, it is not clear what features users currently use. So,
there is bloat in the software that would be put into production. However, the
critical problem is that few if any will know:
- What's working?
- What isn't working?
- Are there any problems with the parts that no one knows about?

## Strategy for upgrading Django and Python

UIPA.org was built with a modified Froide repository to handle a change in web
page for making FOI requests. Since that time, no upstream changes have been
incorportated. Thus, the forked Froide repository is frozen in time.

This means that we don't really need to keep it separate and can incorporate it
into the UIPA.org repo as included Django apps instead of an editable
dependency.

Another dependency, `django-overextends`, can be eliminated because it's
functionality was included in Django 1.9.

The [Django 1.9 Release
Notes](https://docs.djangoproject.com/en/5.1/releases/1.9/) says:
- Django template loaders can now extend templates recursively. (See
[Templates](https://docs.djangoproject.com/en/5.1/releases/1.9/#templates)).
- Django template loaders have been updated to allow recursive template
extending. This change necessitated a new template loader API. The old
load_template() and load_template_sources() methods are now deprecated. Details
about the new API can be found in the template loader documentation. (See
[Template loader APIs have
changed](https://docs.djangoproject.com/en/5.1/releases/1.9/#template-loader-apis-have-changed)).

This is further supported by PR
[#9884](https://github.com/django/django/pull/9884) which adds documentation
about this.
- [@unexceptable's comment on August 12,
  2019](https://github.com/django/django/pull/9884#issuecomment-520636912) says:
    > This was added to django 1.9, but before then many of us got by using:
    > [https://github.com/stephenmcd/django-overextends](https://github.com/stephenmcd/django-overextends)

See the Django 1.11 [Overriding
templates](https://docs.djangoproject.com/en/1.11/howto/overriding-templates/).

## Supported versions of Django and Python

### [Django](https://www.djangoproject.com/download/#supported-versions)

| Version | Latest Release | End of Mainstream Support | End of Extended Support |
| :--- | :--- | :--- | :--- |
| Django 5.2 LTS  | Coming April 2025 | December 2025 | April 2028 |
| Django 5.1      | 5.1.4   | April 2025 | December 2025 |
| Django 4.2 LTS  | 4.2.17  | 12/04/2024 | April 2026 |
| Django 3.2 LTS  | 3.2.25  | 12/07/2021 | April 2024 |
| Django 2.2 LTS  | 2.2.28  | 12/02/2019 | April 2022 |
| Django 1.11 LTS | 1.11.29 | 12/02/2017 | April 2020 |


### [Python](https://devguide.python.org/versions/#supported-versions)

| Version | Latest Release | End of Support |
| :--- | :--- | :--- |
| Python 3.13 | 3.13.1 (12/03/2024) | October 2029 |
| Python 3.12 | 3.12.8 (12/03/2024) | October 2028 |
| Python 3.11 | 3.11.11 (12/03/2024 source only) | October 2027 |
| Python 3.10 | 3.10.16 (12/03/2024 source only) | October 2026 |
| Python 3.9 | 3.9.21 (12/03/2024 source only) | October 2025 |
| Python 3.8 | 3.8.20 (09/06/2024 source only) | October 2024 |

## Repositories

| Repositories | URL                                     | Branch | Forked from |
| :---         | :---                                    | :---   | :--- |
| UIPA         | https://github.com/CodeWithAloha/uipa   | master | https://github.com/okfde/froide-theme |
| Froide       | https://github.com/CodeWithAloha/froide | master | https://github.com/okfde/froide |

UIPA.org was built from a fork of the Froide Theme repo that was renamed to
`uipa`. It's not the only repo. Careful reading of the `README` and the
`requirements.txt` files reveals that Froide is arranged as an editable
dependency (`pip install -r requirements.txt -e . --src=./src`) for UIPA.org.

One of the reasons the Froide repo was forked was because the `FoiRequest`
module was modified to accommodate asking a requester to state why they should
have the fees waived. This was a requirement from the [UIPA request
form](https://oip.hawaii.gov/forms/) provided by the [Office of Information
Practices](https://oip.hawaii.gov/).

The commit history shows that there were other mods made to Froide.

```shell
froide (master)$ git remote -v
origin	https://github.com/CodeWithAloha/froide (fetch)
origin	https://github.com/CodeWithAloha/froide (push)

froide (master)$ git branch
* master

froide (master)$ git log --pretty='format:%h%d (%cn %as, %s)' -n 10
03c6a1f1 (HEAD -> master, origin/master) (Ryan 2018-10-11, Added cc logic to foirequest model)
4df7f378 (Ryan 2017-11-18, Extended length of cached front page)
c47a3330 (Ryan 2017-07-07, Removed form1_records_request.pdf checks. Instead, changed attachment to can_approve=False)
7ef92270 (Ryan 2017-06-24, Parse deferred using postmark)
51dd9a03 (Ryan 2017-06-24, Unsure how this reprocess would ever have worked, tbh)
31f9446e (Ryan 2017-06-24, Added more logging for Deferred)
22a8e374 (Ryan 2017-06-24, Added _deliver_mail logging for Deferred Messages)
5f78b01b (Ryan 2017-06-24, Added logging for deferred admin)
3ba1c960 (Ryan 2017-06-24, Added logging to figure out why deferreds are silently being eaten)
e2ff2b25 (Ryan 2017-06-24, Updated subject to remove word 'one')
```

### What version of Froide was the UIPA.org forked from?

It looks like v3.0 (03/14/2013) of okfde/froide was used as the starting point.

```shell
froide (master)$ git remote -v
origin	https://github.com/CodeWithAloha/froide (fetch)
origin	https://github.com/CodeWithAloha/froide (push)

froide (master)$ git branch
* master

froide (master)$ git log --pretty='format:%h%d (%cn %as, %s)' --tags --no-walk
066cc4a2 (tag: v3.0) (Stefan Wehrmeyer 2013-03-14, Bump to version 3.0)
00ec1650 (tag: v2.0) (Stefan Wehrmeyer 2012-10-05, Make public body number static on Hamburg for now)


froide (master)$ git log --pretty='format:%h%d (%cn %as, %s)' --tags | sed 5
066cc4a2 (tag: v3.0) (Stefan Wehrmeyer 2013-03-14, Bump to version 3.0)
7343ec7b (Stefan Wehrmeyer 2013-03-14, Update translation files)
6ab9b6e0 (Stefan Wehrmeyer 2013-03-14, Move set status template around)
0d04cdd6 (Stefan Wehrmeyer 2013-03-14, Fix dependency of moved repository)
f781e3dd (Stefan Wehrmeyer 2013-03-13, Add test data for last commit)


  * Some commits after v3.0:

1d138ef9 (Stefan Wehrmeyer 2013-04-18, Merge pull request #51 from felixebert/master)
3c93f486 (Felix Ebert 2013-04-17, Issue #50: update of ScrollToFixed plugin (for minWidth property))
23621de9 (Felix Ebert 2013-04-17, fix for Issue #50: Mobile: Section "Ähnliche Anfrage" overlays request content area)
36ff6f9e (Stefan Wehrmeyer 2013-04-10, Add features to DeferredMessage admin)
ca708d1f (Stefan Wehrmeyer 2013-04-06, Fix check same request tag)
5218285b (Stefan Wehrmeyer 2013-04-02, Fix email name replacement)
```

Tags on Froide's main branch.

```shell
froide (main)$ git remote -v
origin	https://github.com/okfde/froide (fetch)
origin	https://github.com/okfde/froide (push)

froide (main)$ git branch
* main

froide (main)$ git log --pretty='format:%h%d (%cn %as, %s)' --tags --no-walk
cb21c3a9 (tag: v5.0.0) (Stefan Wehrmeyer 2018-09-03, Bump version to 5.0.0)
066cc4a2 (tag: v3.0) (Stefan Wehrmeyer 2013-03-14, Bump to version 3.0)
00ec1650 (tag: v2.0) (Stefan Wehrmeyer 2012-10-05, Make public body number static on Hamburg for now)
77d7f8bf (tag: django-1.4) (Stefan Wehrmeyer 2012-09-01, Update requirements for Django 1.4)
```

### Repos for this upgrade

| Repositories | URL  | Branch |
| :---         | :--- | :---   |
| UIPA   | https://github.com/CodeWithAloha/uipa   | master |
| Froide | https://github.com/CodeWithAloha/froide | master |

## Error loading User model (06/04/2024)

***FIXED!***

### The FIX
This problem is due to the Froide account User model trying to provide a method
to return the SetPasswordForm for the views. The fix is to remove
SetPasswordForm from froide/account/models.py and add it to
froide/account/views.py.

### The problem

When trying to upgrade Django from 1.10.2 (last working UIPA) to 1.11, running
"python manage.py check" fails with an error about the "AUTH_USER_MODEL refers
to model 'account.User' that has not been installed". This is prevent further
progress in upgrading Django and Python.

~~The final conclusion is the old UIPA can't be upgraded so a new UIPA will need
to be created with the current version of Froide.~~

It is possible to change the use of Froide from an installed source dependency
to being a part of the UIPA (Froide Theme) code base. This may make it easier
to mold the newer Froide (Django 4.2) to what UIPA needs by removing froide
apps that may not be useful.

```shell
(venv2) uipa (upgrade-master)$ python manage.py check
Traceback (most recent call last):
  File "manage.py", line 11, in <module>
    execute_from_command_line(sys.argv)
  File "/Users/russ/Projects/Code_With_Aloha/Code_for_Hawaii/update-old/last_working/uipa/venv2/lib/python2.7/site-packages/django/core/management/__init__.py", line 363, in execute_from_command_line
    utility.execute()
  File "/Users/russ/Projects/Code_With_Aloha/Code_for_Hawaii/update-old/last_working/uipa/venv2/lib/python2.7/site-packages/django/core/management/__init__.py", line 337, in execute
    django.setup()
  File "/Users/russ/Projects/Code_With_Aloha/Code_for_Hawaii/update-old/last_working/uipa/venv2/lib/python2.7/site-packages/django/__init__.py", line 27, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/Users/russ/Projects/Code_With_Aloha/Code_for_Hawaii/update-old/last_working/uipa/venv2/lib/python2.7/site-packages/django/apps/registry.py", line 108, in populate
    app_config.import_models()
  File "/Users/russ/Projects/Code_With_Aloha/Code_for_Hawaii/update-old/last_working/uipa/venv2/lib/python2.7/site-packages/django/apps/config.py", line 202, in import_models
    self.models_module = import_module(models_module_name)
  File "/Users/russ/micromamba/envs/py2/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/russ/Projects/Code_With_Aloha/Code_for_Hawaii/update-old/last_working/uipa/froide/account/models.py", line 18, in <module>
    from django.contrib.auth.forms import SetPasswordForm
  File "/Users/russ/Projects/Code_With_Aloha/Code_for_Hawaii/update-old/last_working/uipa/venv2/lib/python2.7/site-packages/django/contrib/auth/forms.py", line 22, in <module>
    UserModel = get_user_model()
  File "/Users/russ/Projects/Code_With_Aloha/Code_for_Hawaii/update-old/last_working/uipa/venv2/lib/python2.7/site-packages/django/contrib/auth/__init__.py", line 194, in get_user_model
    "AUTH_USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL
django.core.exceptions.ImproperlyConfigured: AUTH_USER_MODEL refers to model 'account.User' that has not been installed
```

