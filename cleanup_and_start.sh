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
    sudo apt-get install -y python3
else
    echo "Python3 is already installed."
fi

# Ensure tmux is installed
if ! command -v tmux &> /dev/null; then
    echo "tmux could not be found. Installing..."
    sudo apt-get update
    sudo apt-get install -y tmux
else
    echo "tmux is already installed."
fi

# Log tmux version
tmux -V

# Run Docker Compose in a new tmux session and log the output
tmux new-session -d -s docker_session 'docker-compose up -d > /tmp/docker_compose.log 2>&1'

# Wait and check if the tmux session is still running
sleep 10
tmux list-sessions

# Log the output
tmux capture-pane -t docker_session -p > /tmp/docker_session_output.log

# Check if services are running
docker ps > /tmp/docker_ps.log
