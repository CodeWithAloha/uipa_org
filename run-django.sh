#!/bin/ash

export GDAL_LIBRARY_PATH='/usr/lib/libgdal.so.34'
export GEOS_LIBRARY_PATH='/usr/lib/libgeos_c.so.1'
python ./manage.py diffsettings --all
python ./manage.py runserver  0.0.0.0:8000