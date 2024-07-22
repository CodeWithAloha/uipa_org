# Use any Debian/Ubuntu based image
FROM mcr.microsoft.com/vscode/devcontainers/base:bullseye

# root access for the beginning of the script
USER root

# Install system-wide dependencies that cannot be done in a venv
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
        libpoppler-cpp-dev \
        python-is-python3 \
        gdal-bin \
        libgdal-dev \
        imagemagick \
        libmagickwand-dev \
        python3-dev \
        pkg-config \
        build-essential \
        python3-venv \
        libproj-dev \
        proj-data \
        proj-bin \
        libgeos-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Optional arguments
ARG INSTALL_ZSH="true"
ARG UPGRADE_PACKAGES="false"
ARG ENABLE_NONROOT_DOCKER="true"
ARG USE_MOBY="true"

# Enable new "BUILDKIT" mode for Docker CLI
ENV DOCKER_BUILDKIT=1

# Install needed packages and setup non-root user
ARG USERNAME=automatic
ARG USER_UID=1000
ARG USER_GID=$USER_UID

COPY .devcontainer/library-scripts/ /tmp/library-scripts/

RUN apt-get update \
    && /bin/bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "true" "true" \
    && /bin/bash /tmp/library-scripts/docker-debian.sh "${ENABLE_NONROOT_DOCKER}" "/var/run/docker-host.sock" "/var/run/docker.sock" "${USERNAME}" \
    && groupadd -r baseuser && useradd -r -g baseuser baseuser \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts/

# Create directories for Elasticsearch and add necessary permissions
RUN mkdir -p /usr/share/elasticsearch /var/lib/elasticsearch /var/log/elasticsearch \
    && chown -R baseuser:baseuser /usr/share/elasticsearch /var/lib/elasticsearch /var/log/elasticsearch







    
# Create the static files directory
RUN mkdir -p /home/app/build






WORKDIR /home/app

# Copy your application code from the root directory
# COPY .. /home/app/
COPY . /home/app/

RUN chmod +x /home/app/data/seed/init_db.sh

# Display the contents of codespaces-requirements.txt for debugging
# RUN echo "Displaying codespaces-requirements.txt:" && cat /home/app/codespaces-requirements.txt
RUN echo "Displaying requirements.txt:" && cat /home/app/requirements.txt

# Create the virtual environment
RUN python3 -m venv /home/app/venv

# Debugging: Display directory structure to check if venv is created correctly
RUN ls -R /home/app

# Activate the virtual environment and install dependencies
RUN /bin/bash -c "source /home/app/venv/bin/activate && pip install --upgrade pip && pip install -r /home/app/requirements.txt"

# Debugging: Display Python and pip versions
RUN /bin/bash -c "source /home/app/venv/bin/activate && python --version && pip --version"

# Switch back to the baseuser
USER baseuser

# Setup the app here

# Setting the ENTRYPOINT to docker-init.sh will configure non-root access 
# to the Docker socket. The script will also execute CMD as needed.
# ENTRYPOINT [ "/usr/local/share/docker-init.sh" ]
# ENTRYPOINT [ "/entrypoint.sh" ]

# CMD [ "sleep", "infinity" ]





# might be able to do the pip install for requirements this way as well if this functions correctly
# Run database migrations and start the server
# CMD ["/bin/bash", "-c", "cd .. && source /app/venv/bin/activate && bash data/seed/init_db.sh && python manage.py migrate && python manage.py runserver"]
# CMD ["/bin/bash",]#
# CMD [ "sleep", "infinity" ]
# Set the CMD to run your application directly
CMD ["/bin/bash", "-c", "source /home/app/venv/bin/activate && bash /home/app/data/seed/init_db.sh && python /home/app/manage.py migrate && python /home/app/manage.py runserver 0.0.0.0:8000"]



# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
