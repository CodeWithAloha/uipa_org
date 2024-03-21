# Seeding the Database

This covers seeding the database for development work.

## Preparation

You should have followed the steps for getting started and have:

- PostgreSQL database and Elasticsearch search engine running in Docker containers.
- Vite front end server running in another terminal window.
- Django development server running in another terminal window.

At this point, you should be able to login to the Admin website at
http://localhost:8000/ or http:127.0.0.1:8000/ with the email address and
password of the super user you created.

In a fourth terminal window, have your Python virtual environment activated and
be in your working directory with the UIPA.org source files cloned from your
fork of the main branch of the [UIPA.org
repository](https://github.com/CodeWithAloha/uipa).

## Seeding

To seed the database, run these commands:

```
$ python manage.py loaddata data/seed/new-classification.json                                
$ python manage.py loaddata data/seed/new-jurisdiction.json                                  
$ python manage.py loaddata data/seed/new-foilaw.json                                        
```

This will set up the data that needs to exist in the database before you upload
the public body information from a CSV file.

For the first time that you seed the database, you'll be using a very small
subset of data to see how things go.

Run this commands load the category data that's needed to load the subset of
public body data:

```
$ python manage.py loaddata data/seed/new-category.json
```

Then, on the `Public Body` page (Home > Public Body > Public Bodies), scroll
down to the bottom of the page to where there is a `Choose File` button next to
the `Import Public Bodies` button.

Click on the `Choose File` button and navigate to the directory with
`test-public-bodies.csv` file. Select that file and click on the `Open` button.

Back on the `Public Body` page, click on the `Import Public Bodies` button.

If this works, you should see a message on the `Public Body` page that says
that the public bodies were imported.

## Seeding with all public bodies

If the first time seeding the database with the very small set of data works,
you can load the full set of public bodies.

Stop your Django server by pressing Ctl-C in the terminal window running the server.

Run these commands to re-initialize the database:

```
$ sh data/seed/clear_db.sh
$ sh data/seed/init_db.sh
```

To load the full set of data, you'll need to prepare an export of data from the
production UIPA.org website. The exported data will be in a CSV file.

### Preparing a CSV file to upload public bodies

You'll need to:

- Generate a fixture file in JSON format with the tag values from the `tags`
  field of the exported CSV file.

  TODO: Run a Python script to generate the category.json fixture file.

- Generated a new CSV file to upload to your Admin website.
    - The `tags` field should be renamed to `categories`.
    - The data in the `categories` field must not have spaces following the
      commas that separate multiple category values.

### Loading public bodies

After the new category.json fixture file has been created, run this command:

```
$ python manage.py loaddata data/seed/category.json
```
This assumes that the category.json file is in the `data/seed` directory.

Next, go the `Public Body` page (Home > Public Body > Public Bodies) and upload
the new CSV file.

