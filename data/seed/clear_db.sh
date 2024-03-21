#!/bin/bash
# clear_db.sh - Clear out all of the data from the database including migrations info
#               and search index. Use this to "reset" the database so the
#               initial migrations can be run.
#
# Ref: https://docs.djangoproject.com/en/4.2/ref/django-admin/#flush
#

echo "Drop and recreate the database..."
#  PostgreSQL-specific commands.
python manage.py dbshell << EOF
\c postgres;
drop database froide;
create database froide owner froide;
EOF

echo "Clear the search index..."
#  This command will prompt interactively for confirmation.
python manage.py search_index --delete

