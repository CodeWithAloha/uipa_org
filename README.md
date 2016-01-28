[![Stories in Ready](https://badge.waffle.io/codeforhawaii/uipa_org.png?label=ready&title=Ready)](https://waffle.io/codeforhawaii/uipa_org)

# UIPA.org - Uniform Information Practices Act portal

This is a basic Django project with a theme app that plugs into [Froide](https://github.com/stefanw/froide). It's based on the [Froide Base Theme](https://github.com/okfde/froide-theme).

## Get started easily


In a Python virtualenv run:

    pip install -r requirements.txt -e .
    pip uninstall South (Make sure to uninstall South!)
    python manage.py syncdb  --noinput
    python manage.py createsuperuser
    python manage.py runserver

Be sure to remember the password for the admin user you created in the last command above. You will need it to create pages later.

[Here is a complete guide of how to set this up on Heroku.](http://froide.readthedocs.org/en/latest/herokudeployment/)


## Froide documentation

http://froide.readthedocs.org/en/latest/gettingstarted/

For details about working with Froide Themes see [Theming Froide](http://froide.readthedocs.org/en/latest/theming/).


## Creating page content for the About, Help, Terms of Use, and Privacy Statement links

Django Flat Pages are used to create these pages. They are "flat" HTML content stored in the database. For details, see [The flatpages app](https://docs.djangoproject.com/es/1.9/ref/contrib/flatpages/) documentation.

To create these pages initially, we:

* Create the pages using the Django administration interface at http://localhost:8000/uipa-admin/. Click on the *Flat pages* link.
* Dump the database in JSON format (see below).
* Edit the dump file, **db-dump.json**.
* Copy the section of JSON data for the model, "flatpages.flatpage" (see below).
* Put the JSON data in a file under the fixtures directory named **\<page\>.json**. For example, **about.json** for the About page.


### Loading the page data

Once the page data files have been created under the fixtures directory, they can be loaded whenever a new instance of uipa.org is created. This is done by loading the page data files using this command:

```
python manage.py loaddata <page> \[<page>\]
```
where **\<page\>** is the name of the page data file without the **.json** extension. Multiple pages can be loaded at the same time.


### Dumping the database

Dumping the database in JSON format is done using the command:

```
python manage.py dumpdata | python -m json.tool > db-dump.json
```


### Page data in JSON format

Here's an example of the page data in JSON format for the About page:

```
{
    "fields": {
        "content": "UIPA is the place where you can request information from your government.",
        "enable_comments": false,
        "registration_required": false,
        "sites": [
            1
        ],
        "template_name": "help/page.html",
        "title": "About UIPA",
        "url": "/help/about/"
    },
    "model": "flatpages.flatpage",
    "pk": 1
}
```


## License

Froide Theme is licensed under the MIT License.
