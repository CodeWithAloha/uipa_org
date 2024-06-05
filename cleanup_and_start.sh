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

# Run Docker Compose with detailed logs
docker-compose up -d
