#!/bin/bash

# Update the package list
sudo apt-get update

# Install required packages
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common gnupg

# Download and run Docker's official installation script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Verify Docker installation
docker --version

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verify Docker Compose installation
docker-compose --version

# Add the current user to the Docker group
sudo usermod -aG docker $USER

# Start Docker daemon
sudo service docker start

# Create a new session with Docker group permissions
newgrp docker
