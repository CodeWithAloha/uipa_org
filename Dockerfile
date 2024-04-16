FROM ssthapa/django5:0.1

MAINTAINER Suchandra Thapa <suchandra.spam+docker@gmail.com>

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100


COPY pyproject.toml /srv/django/pyproject.toml

RUN apk update && \
    apk add rust cargo qpdf qpdf-dev poppler poppler-dev g++ gdal geos alpine-sdk \
            imagemagick imagemagick-dev pango nodejs npm yarn

ENV PYTHONPATH "${PYTHONPATH}:/srv/django"
WORKDIR /srv/django
COPY . /srv/django
RUN yarn link && yarn link uipa_org && yarn install
RUN /root/.local/bin/poetry config installer.max-workers 3
RUN /root/.local/bin/poetry install --no-root --no-interaction


COPY local_settings.py /srv/django/uipa_org/settings/local_settings.py
COPY settings.py /srv/django/uipa_org/settings/settings.py
COPY run-backend.sh /srv/django

ENTRYPOINT  /srv/django/run-backend.sh

