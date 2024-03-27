#!/bin/bash
# load_fixtures.sh - Load the database from the fixtures and CSV file.
#

ST=$(date)
echo "Loading from fixtures..."
python manage.py loaddata data/seed/2024-03-21-classification.json 
python manage.py loaddata data/seed/2024-03-21-jurisdiction.json 
python manage.py loaddata data/seed/2024-03-24-categories.json 
python manage.py loaddata data/seed/2024-03-21-foilaw.json 

echo "Done:  $(date)"
echo "Start: $ST"
