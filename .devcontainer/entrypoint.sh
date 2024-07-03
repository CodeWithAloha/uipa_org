#!/bin/bash

echo "Starting entrypoint script..."

# Navigate to the project root directory
echo "Changing directory to project root..."
cd ..

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Run the initial setup script
echo "Running initial setup script..."
if bash data/seed/init_db.sh; then
    echo "Initial setup script completed successfully."
else
    echo "Initial setup script failed." >&2
    exit 1
fi

# Check the Django project
echo "Checking Django project..."
if python manage.py check; then
    echo "Django project check completed successfully."
else
    echo "Django project check failed." >&2
    exit 1
fi

# Apply database migrations
echo "Applying database migrations..."
if python manage.py migrate; then
    echo "Database migrations applied successfully."
else
    echo "Database migrations failed." >&2
    exit 1
fi

# Start the development server
echo "Starting the development server..."
if python manage.py runserver 0.0.0.0:8000; then
    echo "Development server started successfully."
else
    echo "Failed to start the development server." >&2
    exit 1
fi
