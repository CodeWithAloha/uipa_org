#!/bin/bash

# Navigate to the project root directory
cd ..

# Activate the virtual environment
source venv/bin/activate

# Run the initial setup script
bash data/seed/init_db.sh

python manage.py check

# Apply database migrations
# python manage.py migrate

# Start the development server
# python manage.py runserver 0.0.0.0:8000
python manage.py runserver
