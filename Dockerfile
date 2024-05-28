ARG VARIANT="16"
FROM mcr.microsoft.com/devcontainers/javascript-node:1-${VARIANT}

# Install dependencies
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
    docker-compose \
    sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# [Optional] Uncomment if you want to install an additional version of node using nvm
# ARG EXTRA_NODE_VERSION=18
# RUN su node -c "source /usr/local/share/nvm/nvm.sh && nvm install ${EXTRA_NODE_VERSION}"
