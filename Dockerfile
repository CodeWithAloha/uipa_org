ARG VARIANT="16"
FROM mcr.microsoft.com/devcontainers/javascript-node:1-${VARIANT}

# Install dependencies
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get install -y --no-install-recommends \
#     libqpdf-dev \
#     g++ \
#     wget \
#     python3-pip \
#     python3-psycopg2 \
#     python3-lxml \
#     libxml2-dev \
#     libpq-dev \
#     libgdal-dev \
#     imagemagick \
#     git \
#     libpangocairo-1.0-0 \
#     libmagic1 \
#     docker-compose \
#     sudo \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*


RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl software-properties-common gnupg && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu focal stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
    usermod -aG docker vscode

# Expose ports (if necessary)
# EXPOSE 8000 5432 9200

# Start Docker daemon
CMD ["sudo", "service", "docker", "start"]

# [Optional] Uncomment if you want to install an additional version of node using nvm
# ARG EXTRA_NODE_VERSION=18
# RUN su node -c "source /usr/local/share/nvm/nvm.sh && nvm install ${EXTRA_NODE_VERSION}"
