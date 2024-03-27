#!/bin/bash
# init_db.sh - Initialize the database to the point before uploading public
#              body data.
#

echo "Running initial migration..."
python manage.py migrate

echo
echo "Creating and populating the search index..."
python manage.py search_index --create
python manage.py search_index --populate

echo
echo "Changing the site name to uipa.org..."
python manage.py dbshell -- -c "update django_site set domain = 'uipa.org', name = 'uipa.org' where id = 1;"

echo
echo "Create a super user..."
python manage.py createsuperuser

