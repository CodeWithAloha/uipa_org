#!/bin/bash

# Clean up Docker system
docker system prune -a -f
docker volume prune -f

# Start Docker service
sudo service docker start

# Run Docker Compose with detailed logs
docker-compose up --build
