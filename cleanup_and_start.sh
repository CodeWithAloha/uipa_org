#!/bin/bash

# Clean up Docker system
docker system prune -a -f
docker volume prune -f

# Start Docker service
sudo service docker start

# Wait for Docker daemon to start
sleep 10

# Run Docker Compose with detailed logs
docker-compose up -d
