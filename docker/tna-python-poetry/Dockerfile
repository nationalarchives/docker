# FROM ghcr.io/nationalarchives/tna-python:latest
FROM tna-python

ENV POETRY_HOME=/home/app/.local \
    POETRY_VERSION=1.4.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true

COPY --chown=app:app bin/tna-build .local/bin/
RUN chmod +x .local/bin/tna-build

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL "https://install.python-poetry.org" | python -
