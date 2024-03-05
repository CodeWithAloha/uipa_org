#ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-3.8.12}
#FROM python:${INSTALL_PYTHON_VERSION}-slim-bullseye AS base
# FROM debian:bullseye-slim AS base
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
            imagemagick imagemagick-dev pango

ENV PYTHONPATH "${PYTHONPATH}:/srv/django"
WORKDIR /srv/django

RUN /root/.local/bin/poetry install

COPY ./froide /srv/django

COPY run-backend.sh /srv/django
ENTRYPOINT  /srv/django/run-backend.sh

