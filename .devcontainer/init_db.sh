#!/bin/bash
# init_db.sh - Initialize the database to the point before uploading public
#              body data.
#

echo "Run initial migration..."
python manage.py migrate

echo
echo "Create and populate the search index..."
python manage.py search_index --populate

echo
echo "Load the seed data..."
python manage.py loaddata uipa_org/fixtures/*

echo
echo "Now you can start the dev web server."
