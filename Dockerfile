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
COPY ./froide /srv/django
RUN cd froide && yarn link && yarn link froide && yarn install
RUN /root/.local/bin/poetry install


COPY local_settings.py /srv/django/froide/local_settings.py
COPY settings.py /srv/django/froide/settings.py
COPY run-backend.sh /srv/django

ENTRYPOINT  /srv/django/run-backend.sh

