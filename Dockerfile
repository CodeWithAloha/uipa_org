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
        libpoppler-cpp-dev \
        cmake \
        build-essential \
        pkg-config \
        meson \
        ninja-build \
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

# Set up the working directory
WORKDIR /workspace

# Create and activate a virtual environment
RUN python3 -m venv /workspace/venv

# Upgrade pip
RUN /workspace/venv/bin/pip install --upgrade pip

# Install dependencies in smaller groups to identify the problematic package
RUN /workspace/venv/bin/pip install \
        django==4.2.4 \
        Markdown==3.4.3 \
        celery==5.2.7 \
        django-celery-email==3.0.0 \
    && /workspace/venv/bin/pip install \
        django-taggit==4.0.0 \
        pytz==2023.3 \
        requests==2.31.0 \
        django-floppyforms==1.9.0 \
    && /workspace/venv/bin/pip install \
        python-magic==0.4.27 \
        python-mimeparse==1.6.0 \
        django-configurations==2.5.1 \
        django-storages==1.13.2 \
    && /workspace/venv/bin/pip install \
        dj-database-url==2.0.0 \
        django-contrib-comments==2.2.0 \
        unicodecsv==0.14.1 \
        django-tinymce==3.6.1 \
    && /workspace/venv/bin/pip install \
        python-docx==0.8.11 \
        elasticsearch==8.11.1 \
        lxml==5.2.1 \
    && /workspace/venv/bin/pip install \
        channels==4.0.0 \
        django-treebeard==4.4 \
        django-leaflet==0.29.0 \
        django-json-widget==1.1.1 \
    && /workspace/venv/bin/pip install \
        django-celery-beat==2.5.0 \
        django-mfa3==0.11.0 \
        psycopg[binary]==3.1.18 \
        psycopg-binary==3.1.18 \
    && /workspace/venv/bin/pip install \
        oauthlib==3.2.2 \
        django-oauth-toolkit==1.7.1 \
        django-fsm==2.8.1 \
    && /workspace/venv/bin/pip install \
        websockets==11.0.3 \
        bleach==6.0.0 \
    # Install editable packages
    && /workspace/venv/bin/pip install -e git+https://github.com/codewithaloha/froide.git@main#egg=froide \
    && /workspace/venv/bin/pip install -e git+https://github.com/okfde/django-filingcabinet.git@main#egg=django-filingcabinet

# Set environment variables to use the virtual environment by default
ENV VIRTUAL_ENV=/workspace/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Start Docker daemon
CMD ["sudo", "service", "docker", "start"]
