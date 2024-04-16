#!/bin/ash

export GDAL_LIBRARY_PATH='/usr/lib/libgdal.so.34'
export GEOS_LIBRARY_PATH='/usr/lib/libgeos_c.so.1'

#yarn link
#yarn link froide
#yarn install
yarn serve dev &

echo "STARTING DB"
# To initialise the database:
/root/.local/bin/poetry run ./manage.py migrate --skip-checks
# Create a superuser
/root/.local/bin/poetry run ./manage.py createsuperuser
# Create and populate search index
/root/.local/bin/poetry run ./manage.py search_index --create
/root/.local/bin/poetry run ./manage.py search_index --populate

/root/.local/bin/poetry run ./manage.py diffsettings --all
/root/.local/bin/poetry run ./manage.py runserver  0.0.0.0:8000
