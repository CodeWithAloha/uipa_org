ARG VARIANT="16"
FROM mcr.microsoft.com/devcontainers/javascript-node:1-${VARIANT}

# Install main dependencies
RUN apk update && apk add --no-cache \
    libqpdf \
    g++ \
    wget \
    python3 \
    py3-pip \
    postgresql-dev \
    libxml2-dev \
    gdal-dev \
    imagemagick \
    git \
    pango-dev \
    file \
    sudo

# Add Docker Compose
RUN apk add --no-cache docker-compose

# Ensure the vscode user exists and add it to the Docker group
RUN addgroup -S docker && adduser vscode docker

# Expose ports (if necessary)
# EXPOSE 8000 5432 9200

# Start Docker daemon
CMD ["sudo", "service", "docker", "start"]
