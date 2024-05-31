ARG VARIANT="16"
FROM mcr.microsoft.com/devcontainers/javascript-node:1-${VARIANT}

# Install main dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
    libqpdf-dev \
    g++ \
    wget \
    python3-pip \
    python3-psycopg2 \
    python3-lxml \
    libxml2-dev \
    libpq-dev \
    libgdal-dev \
    imagemagick \
    git \
    libpangocairo-1.0-0 \
    libmagic1 \
    sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add Docker's official GPG key
RUN mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Add Docker APT repository
RUN echo \
    "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update APT package sources and install Docker
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
    docker-ce docker-ce-cli containerd.io docker-compose-plugin \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Ensure the vscode user exists and add it to the Docker group
RUN groupadd -f docker && usermod -aG docker vscode || true

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Expose ports (if necessary)
# EXPOSE 8000 5432 9200

# Start Docker daemon
CMD ["sudo", "service", "docker", "start"]

# [Optional] Uncomment if you want to install an additional version of node using nvm
# ARG EXTRA_NODE_VERSION=18
# RUN su node -c "source /usr/local/share/nvm/nvm.sh && nvm install ${EXTRA_NODE_VERSION}"
