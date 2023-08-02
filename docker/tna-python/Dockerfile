# https://hub.docker.com/_/debian/tags?page=1&name=bookworm-slim
# https://hub.docker.com/_/python/tags?page=1&name=3.11-slim
FROM python:3.11-slim

ARG version

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    ENVIRONMENT=production \
    POETRY_HOME=/home/app/.local \
    POETRY_VERSION=1.5.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends curl=7.88.1-10 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL "https://install.python-poetry.org" | python -

RUN useradd --create-home app
USER app
WORKDIR /home/app

COPY --chown=app bin/tna-build bin/tna-run .local/bin/
RUN chmod +x .local/bin/tna-build .local/bin/tna-run
ENV PATH="/home/app/.local/bin:$PATH"

LABEL version="${version}" \
    org.opencontainers.image.description="National Archives base Docker image"
EXPOSE 8080/tcp
# HEALTHCHECK CMD curl --fail http://localhost:8000/healthcheck/ || exit 1
