# Seeding the Database

This covers seeding the database for development work.

## Preparation

You should have followed the steps for getting started and have:

- PostgreSQL database and Elasticsearch search engine running in Docker
  containers in one terminal window.
- Vite front end server running in another terminal window.
- Django development server running in another terminal window.

At this point, you should be able to login to the Admin website at:

- http://localhost:8000/admin/
- or http:127.0.0.1:8000/admin/

with the email address and password of the super user you created.

In a fourth terminal window, have your Python virtual environment activated and
be in your working directory with the UIPA.org source files cloned from your
fork of the main branch of the [UIPA.org
repository](https://github.com/CodeWithAloha/uipa).

## Seeding

### Load Classifications, Jurisdictions, and Freedom of Information Laws

Three fixtures will be used to load seed data that is not going to change very
much for development work.

This will set up the data that needs to exist in the database before you upload
the public body information from a CSV file.

```
$ python manage.py loaddata data/seed/2024-03-15-classification.json
$ python manage.py loaddata data/seed/2024-03-15-jurisdiction.json
$ python manage.py loaddata data/seed/2024-03-15-foilaw.json
```

*NOTE:*

> The Classifications data has been extracted from the Classifications field in
> the extract of public bodies from the production UIPA.org website on
> 03/15/2024. See 2024-03-15-Hawaii_UIPA_Public_Bodies_All.csv.


### First Test Load of Public Bodies

For the first time that you seed the database, you'll be using a very small
subset of data to see how things go.

- Run this command to load the category data that's needed to load the subset
  of public body data:

    ```
    $ python manage.py loaddata data/seed/test-categories.json
    ```
- Run this command to load the subset of public body data:

    ```
    $ python manage.py import_csv data/seed/test-public-bodies.csv
    ```

#### Loading public bodies via the Admin website

You can also use the Admin website to load public bodies from a CSV file.

- On the `Public Body` page (Home > Public Body > Public Bodies), scroll
  down to the bottom of the page to where there is a `Choose File` button next
  to the `Import Public Bodies` button.

- Click on the `Choose File` button and navigate to the directory with
  your CSV file. Select that file and click on the `Open` button.

- Back on the `Public Body` page, click on the `Import Public Bodies` button.

- If this works, you should see a message on the `Public Body` page that says
  that the public bodies were imported.


### Loading all public bodies

If the first test loading of the database with the very small set of data works,
you can load the full set of public bodies.

- Stop your Django server by pressing Ctl-C in the terminal window running the
  server.

- Run these commands to re-initialize the database:

    ```
    $ sh data/seed/clear_db.sh
    $ sh data/seed/init_db.sh
    ```

- To load a full set of data, you can use these files:
    - 2024-03-24-categories.json
    - 2024-03-24-public-bodies-fixed.csv

- Load the categories:
    ```
    $ python manage.py loaddata data/seed/2024-03-24-categories.json
    ```
- Load the public bodies:
    ```
    $ python manage.py import_csv data/seed/2024-03-24-public-bodies-fixed.csv
    ```

At this point, you should have all of the basic data from UIPA.org without any
requests and other data.

*NOTE:*

> When loading the public bodies from a CSV file, not all of them are loaded.
> There's a bug in the CSV importer that messes up the slug for the name. This
> causes public bodies with parents to not be loaded and stops with an error
> message about "PublicBody matching query does not exist".
>
> To overcome this, on the Admin website, delete all of the public bodies
> loaded and load the public bodies from the CSV file. Repeat this process a
> couple more times until you see all 201 public bodies loaded. Spot check that
> the slug matches the name by visiting the details of a public body.


### Convenience scripts

For convenience, you run these shell scripts to load the fixture files and
public bodies:

```
$ sh data/seed/load_fixtures.sh
$ sh data/seed/load_public_bodies.sh
```

## Preparing a CSV file to upload public bodies

If you're going to be using a different CSV extract of public bodies, you'll
need to:

- Extract the tag values from the old `tags` field in the exported public
  bodies CSV file.

    ```
    $ python extract_sets.py ../2024-03-15-Hawaii_UIPA_Public_Bodies_All.csv
    ```

  These files are created.
        - parent_names.txt
        - tag_values.txt
        - jurisdiction_slugs.txt
        - classifications.txt
        - public-bodies-fixed.csv
    ```

- We'll be using a unique set of tag values to load into the Category table.

    ```
    $ sort -uf tag_values.txt > utags.txt
    ```

- Generate a fixture file in JSON format with the tag values from the `tags`
  field of the exported CSV file. Rename the fixture file to `categories.json`.

    ```
    $ python gen_categories_fixture.py utags.txt

    $ mv utags.json categories.json

    $ sed 5q categories.json
    [
    {
        "model": "publicbody.category",
        "fields": {
            "name": "Access Hawaii Committee",
    ```

- Find the tag values that need to be changed in the generated CSV file to make
  sure that the Categories values match the categories.json fixture file.

    ```
    $ sort -f tag_values.txt > stags.txt

    $ diff utags.txt stags.txt | grep '>' | sed 's/> //'
    building board of appeals
    civil service
    dbedt
    governor
    liquor control adjudication board
    liquor control commission
    merit appeals board
    planning commission
    police commission
    transportation commission
    ```
  Based on what we found, we must change "building board of appeals" to
  "Building Board of Appeals". The other values must also be changed.


- Edit the new CSV file, public-bodies-fixed.csv, to correct the records that
  have duplicate lower-case values. To find those records, use the `cgrep.py` program.

  Make sure that there are no spaces after the commas that separate multiple
  values in the categories field.

    ```
    $ python cgrep.py "public board of appeals" categories public-bodies-fixed.csv
    id: 94 => "building board of appeals","design advisory committee","geographic information systems","land use","planning commission","zoning board of appeals",DPP,GIS,building,design,development,permitting,planning,zoning
    Found 1 records

    $ python cgrep.py "Building Board of Appeals" categories public-bodies-fixed.csv
    id: 149 => "Arborist Committee","Board of Ethics","Board of Review","Board of Water Supply","Building Board of Appeals","Charter Review Commission","Civil Service Commission","Committee on the Status of Women","Cost Control Commission","Fire Commission","Historic Preservation Commission","Liquor Control Commission","Mayor's Advisory Committee for Equal Access","Open Space Commission","Planning Commission","Police Commission","Salary Commission","civil service","financial disclosure","land use",boards,commissions,ethics,fire,gifts,investigation,liquor,lobbying,planning,police,tax,water
    Found 1 records
    ```

