#!/bin/bash

# Set COMPOSE_HTTP_TIMEOUT to ensure Docker Compose waits long enough
export COMPOSE_HTTP_TIMEOUT=200

# Clean up Docker system
docker system prune -a -f
docker volume prune -f

# Start Docker service
sudo service docker start

# Wait for Docker daemon to start
sleep 10

# Ensure Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 could not be found. Installing..."
    sudo apt-get update
    sudo apt-get install -y python3 python-is-python3
else
    echo "Python3 is already installed."
fi

# Verify Python installation
if ! command -v python &> /dev/null; then
    echo "Python is still not available after installation."
else
    python --version
fi

# Activate virtual environment
# source /workspace/venv/bin/activate

# Run Docker Compose with detailed logs
docker-compose up -d
