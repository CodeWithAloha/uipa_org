#!/bin/bash
# clear_db.sh - Clear out all of the data from the database including migrations info
#               and search index. Use this to "reset" the database so the
#               initial migrations can be run.
#
# Ref: https://docs.djangoproject.com/en/4.2/ref/django-admin/#flush
#

echo "Delete and recreate the database..."
#  PostgreSQL-specific commands.
python manage.py dbshell << EOF
\c postgres;
drop database froide;
create database froide owner froide;
EOF

echo
echo "Delete the search index..."
#  Use -f to avoid interactively prompting for confirmation.
python manage.py search_index --delete -f

echo
echo "Now you can run the database migrations and load the seed data."
