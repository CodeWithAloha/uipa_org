#!/bin/bash
# load_public_bodies.sh - Load public bodies from a CSV file.
#

echo "Loading public bodies from a CSV file..."
ST=$(date)
python manage.py import_csv data/seed/2024-03-24-public-bodies-fixed.csv
echo "Done:  $(date)"
echo "Start: $ST"

