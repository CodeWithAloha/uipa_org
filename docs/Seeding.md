# How to Seed the Database

The phrase, "seed the database", refers to the loading some initial data into a database.

"Public bodies" or "Public agencies" means government agencies that are subject to the Uniform Information Practices Act (UIPA) in Hawaii. These include organizations such as the Department of Land & Natural Resources, Department of Planning & Permitting, and the Office of Information Practices.

## Prerequisites

After following the [Getting Started](Getting-Started.md) guide to get your development environment working, the development database will be loaded with data. You can reset the database so that it doesn't contain the seed data.

> Note: The commands shown in this document should be run in the top level of the working directory where the `manage.py` file is located.

## How the database is seeded

The database is created when you run the `docker-compose up` command in a terminal window. A PostgreSQL database is created when the `db` service is started by that command.

The tables for the UIPA website are created when you run `python manage.py migrate`.

Lastly, the database tables are filled with seed data when you run `bash data/seed/init_db.sh`.

You can start using the dev website after it is started up when you run `python manage.py runserver`.

### Differences from Froide

UIPA is built using the [Froide](https://github.com/okfde/froide) Freedom of Information portal software. You could follow its *README* to get your development environment working. In the part that says to create an administrative user with `python manage.py createsuperuser`, we don't need to do that because the data for an administrative user is loaded from a fixture file when the database is seeded. Also, the comands and the order to run them in are handled by the `data/seed/init_db.sh` shell script. This eliminates many manual commands to run to get a working development website.

## Loading the seed data by individual tables

Data can be manually entered via the Admin website or loaded into the database using fixture files (JSON format). Additionally, data for public bodies can be loaded using a CSV file from the command line or via the Admin website.

Fixture files are created from data that has been entered into the database. See the section below that discusses dumping data from the database.

### Classifications, Jurisdictions, and Freedom of Information Laws

These tables don't have many records so they are easily entered by hand via the Admin website. Their data should entered in this order:

- Classifications
- Jurisdictions
- Freedom of Information Laws



This data must be loaded into the database before the public body data can be loaded.

Use these commands to load the data from fixture files:

```
$ python manage.py loaddata data/seed/YYYY-MM-DD-classification.json
$ python manage.py loaddata data/seed/YYYY-MM-DD-jurisdiction.json
$ python manage.py loaddata data/seed/YYYY-MM-DD-foilaw.json
```

> NOTE: The Classifications data has been extracted from the Classifications field in
> the extract of public bodies from the production UIPA.org website on
> 03/15/2024. See 2024-03-15-Hawaii_UIPA_Public_Bodies_All.csv. Update the
> file names in the command to reflect the JSON files located in data/seed/.

### Categories

In the old UIPA.org website, the software uses *tags* to make it easier for users to find a public body. In the newer version of `Froide` used by the new version of UIPA, the user interface uses the data in the *Category* field instead of the *Tag* field. So, we'll put the old *Tag* data into the new *Category* field.

We must load the *Category* data before loading the public body data.

To load the categories, use this command:

    ```
    $ python manage.py loaddata data/seed/2024-03-24-categories.json
    ```

### Public Bodies (Agencies)

The CSV extract of public bodies from the production UIPA.org can be loaded after it is fixed up. See the section below about preparing a CSV file to load public bodies.

Public body data can be loaded from a CSV file using these methods:

#### Method #1: Command line

Run this command to load the public body data:

    ```
    $ python manage.py import_csv data/seed/2024-03-24-public-bodies-fixed.csv
    ```


#### Method #2: Admin website

- On the `Public Body` page (Home > Public Body > Public Bodies), scroll down to the bottom of the page to where there is a `Choose File` button next to the `Import Public Bodies` button.

- Click on the `Choose File` button and navigate to the directory with your CSV file. Select that file and click on the `Open` button.

- Back on the `Public Body` page, click on the `Import Public Bodies` button.

- If this works, you should see a message on the `Public Body` page that says that the public bodies were imported.

> NOTE: When loading the public bodies from a CSV file, not all of them may be loaded. There's a bug in the CSV importer that prevents all the data from being loaded.
>
> To overcome this, on the Admin website, delete all of the public bodies loaded and load the public bodies from the CSV file. Repeat the loading process for public bodies a couple more times until you see all 201 public bodies loaded. Spot check that the slug matches the name by visiting the details of a public body.

At this point, you should have all of the basic data from UIPA.org without any requests and other data.

## Reset your database

If you make a mistake or receive an error loading data, you can start all over with a *clean* database.

Follow these steps:

- Stop your Django server by pressing Ctl-C in the terminal window running the
  server.

- Run these commands to re-initialize the database:

    ```
    $ bash data/seed/clear_db.sh
    $ python manage.py migrate $ python manage.py search_index --populate
    $ python manage.py loaddata uipa_org/fixtures/sites.site.json
    $ python manage.py loaddata uipa_org/fixtures/account.user.json
    ```

At this point, you can start to load seed data.

## Preparing a CSV file to load public bodies

The CSV extract of public bodies from the old UIPA must be fixed up to match the new UIPA database.

- Extract the *tag* values from the *Tag* column in the CSV file.

    ```
    $ python data/seed/extract_sets.py data/2024-03-15-Hawaii_UIPA_Public_Bodies_All.csv
    ```

  These files are created.
    ```
    - parent_names.txt
    - tag_values.txt
    - jurisdiction_slugs.txt
    - classifications.txt
    - public-bodies-fixed.csv
    ```

- The *tag* values to be loaded into the Category table must be unique.

    ```
    $ sort -uf tag_values.txt > utags.txt
    ```

- Generate a fixture file in JSON format with the tag values from the *tags* field of the CSV file. Rename the fixture file to `categories.json`.

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

- Find the *tag* values that need to be changed in the CSV file to make sure that the Categories values match the categories.json fixture file.

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

Based on what we found, we must change "building board of appeals" to "Building Board of Appeals". There are other values that must be changed.

- Copy the CSV file to `public-bodies-fixed.csv`, and edit it to correct the records that have duplicate lower-case values. Use the `cgrep.py` program to find those records.

  Make sure that there are no spaces after the commas that separate multiple values in the categories field.

    ```
    $ python cgrep.py "board of appeals" categories public-bodies-fixed.csv
    id: 94 => "building board of appeals","design advisory committee","geographic information systems","land use","planning commission","zoning board of appeals",DPP,GIS,building,design,development,permitting,planning,zoning
    Found 1 records

    $ python cgrep.py "Building Board of Appeals" categories public-bodies-fixed.csv
    id: 149 => "Arborist Committee","Board of Ethics","Board of Review","Board of Water Supply","Building Board of Appeals","Charter Review Commission","Civil Service Commission","Committee on the Status of Women","Cost Control Commission","Fire Commission","Historic Preservation Commission","Liquor Control Commission","Mayor's Advisory Committee for Equal Access","Open Space Commission","Planning Commission","Police Commission","Salary Commission","civil service","financial disclosure","land use",boards,commissions,ethics,fire,gifts,investigation,liquor,lobbying,planning,police,tax,water
    Found 1 records
    ```

## Dumping data from the database

Data can be dumped from the database into fixture files. Then the fixture files can be used to load data into an empty database.

The fixture files are in JSON format.

Use these command to create fixture files:

```
$ python manage.py dumpdata account.user --indent 4 -o account.user.json
$ python manage.py dumpdata sites.site --indent 4 -o sites.site.json

$ python manage.py dumpdata publicbody.classification --indent 4 -o publicbody.classification.json
$ python manage.py dumpdata publicbody.jurisdiction --indent 4 -o publicbody.jurisdiction.json
$ python manage.py dumpdata publicbody.foilaw --indent 4 -o publicbody.foilaw.json
$ python manage.py dumpdata publicbody.foilawtranslation --indent 4 -o publicbody.foilawtranslation.json

$ python manage.py dumpdata publicbody.category --indent 4 -o publicbody.category.json
$ python manage.py dumpdata publicbody.publicbody --indent 4 -o publicbody.publicbody.json
$ python manage.py dumpdata publicbody.categorizedpublicbody --indent 4 -o publicbody.categorizedpublicbody.json
```
