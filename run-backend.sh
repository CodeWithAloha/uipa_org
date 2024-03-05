#!/bin/ash

export GDAL_LIBRARY_PATH='/usr/lib/libgdal.so.34'
export GEOS_LIBRARY_PATH='/usr/lib/libgeos_c.so.1'

cp froide/local_settings.py.example froide/local_settings.py
/root/.local/bin/poetry run ./manage.py runserver
