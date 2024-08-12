#!/bin/ash

export GDAL_LIBRARY_PATH='/usr/lib/libgdal.so.34'
export GEOS_LIBRARY_PATH='/usr/lib/libgeos_c.so.1'

python ./manage.py migrate --skip-checks
# Create a superuser
python ./manage.py createsuperuser
# Create and populate search index
pythob ./manage.py search_index --create
python ./manage.py search_index --populate
