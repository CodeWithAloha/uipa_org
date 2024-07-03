# Note: You can use any Debian/Ubuntu based image you want. 
FROM mcr.microsoft.com/vscode/devcontainers/base:bullseye

# root acess for beginning of the script
USER root

# Install main dependencies in one step to reduce layers
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
        libpoppler-cpp-dev \
        python-is-python3 \
        gdal-bin \
        libgdal-dev \
        imagemagick \
        libmagickwand-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# [Option] Install zsh
ARG INSTALL_ZSH="true"
# [Option] Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="false"
# [Option] Enable non-root Docker access in container
ARG ENABLE_NONROOT_DOCKER="true"
# [Option] Use the OSS Moby CLI instead of the licensed Docker CLI
ARG USE_MOBY="true"

# Enable new "BUILDKIT" mode for Docker CLI
ENV DOCKER_BUILDKIT=1

# Install needed packages and setup non-root user. Use a separate RUN statement to add your
# own dependencies. A user of "automatic" attempts to reuse an user ID if one already exists.
ARG USERNAME=automatic
ARG USER_UID=1000
ARG USER_GID=$USER_UID
COPY library-scripts/*.sh /tmp/library-scripts/
RUN apt-get update \
    && /bin/bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "true" "true" \
    # Use Docker script from script library to set things up
    && /bin/bash /tmp/library-scripts/docker-debian.sh "${ENABLE_NONROOT_DOCKER}" "/var/run/docker-host.sock" "/var/run/docker.sock" "${USERNAME}" \
    # Create the baseuser user and group
    && groupadd -r baseuser && useradd -r -g baseuser baseuser \
    # Clean up
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts/

# Create directories for Elasticsearch and add necessary permissions
RUN mkdir -p /usr/share/elasticsearch /var/lib/elasticsearch /var/log/elasticsearch \
    && chown -R baseuser:baseuser /usr/share/elasticsearch /var/lib/elasticsearch /var/log/elasticsearch

    # Copy the requirements file to the working directory
COPY codespaces-requirements.txt .

# Display the contents of requirements.txt for debugging
RUN echo "Displaying requirements.txt:" && cat codespaces-requirements.txt

# Update package list and install pip for Python 3
RUN apt-get update && \
    apt-get install -y python3-pip

# Display Python and pip versions for debugging
RUN python3 --version && pip3 --version

# Upgrade pip
RUN pip3 install --upgrade pip


# Install dependencies globally
RUN pip install -r codespaces-requirements.txt

# Switch back to the baseuser
USER baseuser

# Setup the app here

# Setting the ENTRYPOINT to docker-init.sh will configure non-root access 
# to the Docker socket. The script will also execute CMD as needed.
ENTRYPOINT [ "/usr/local/share/docker-init.sh" ]
CMD [ "sleep", "infinity" ]

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
