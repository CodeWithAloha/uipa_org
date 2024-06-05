ARG VARIANT="16"
# FROM mcr.microsoft.com/devcontainers/javascript-node:1-${VARIANT}
# FROM mcr.microsoft.com/devcontainers/javascript-node:1

FROM mcr.microsoft.com/devcontainers/javascript-node:1-18

# Install main dependencies and Docker in one step to reduce layers
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
        libqpdf-dev \
        g++ \
        wget \
        python3-pip \
        python3-psycopg2 \
        python3-lxml \
        python-is-python3 \
        python3-venv \
        libxml2-dev \
        libpq-dev \
        libgdal-dev \
        imagemagick \
        git \
        libpangocairo-1.0-0 \
        libmagic1 \
        sudo \

    # Add Docker's official GPG key
    && mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
    # Add Docker APT repository
    && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null \
    # Update APT package sources and install Docker
    && apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
        docker-ce \
        docker-ce-cli \
        containerd.io \
    # Install Docker Compose
    && curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && docker-compose --version \
    # Ensure the vscode user exists and add it to the Docker group
    && groupadd -f docker && usermod -aG docker vscode || true \
    # Clean up
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/apt/keyrings/docker.gpg

# Expose ports (if necessary)
# EXPOSE 8000 5432 9200

# Copy the requirements file to the working directory
# COPY requirements.txt /workspace/
COPY requirements.txt .

# Create and activate a virtual environment, then install dependencies
RUN python3 -m venv /workspace/venv \
    && /workspace/venv/bin/pip install --upgrade pip \
    && /workspace/venv/bin/pip install -r requirements.txt

# Set environment variables to use the virtual environment by default
ENV VIRTUAL_ENV=/workspace/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# Start Docker daemon
CMD ["sudo", "service", "docker", "start"]