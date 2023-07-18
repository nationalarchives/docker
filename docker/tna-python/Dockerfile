# https://hub.docker.com/_/debian/tags?page=1&name=bookworm-slim
# https://hub.docker.com/_/python/tags?page=1&name=3.11-slim
FROM python:3.11-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    ENVIRONMENT=production

# RUN apt-get update && \
#     apt-get upgrade -y && \
#     apt-get install -y --no-install-recommends gettext=0.21-12 curl=7.88.1-10 && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/env
RUN python -m venv $VIRTUAL_ENV && \
    pip install --upgrade --no-cache-dir pip==23.1.2 gunicorn==21.1.0

RUN useradd --create-home app
USER app
WORKDIR /home/app

COPY --chown=app bin/tna-build bin/tna-run .local/bin/
RUN chmod +x .local/bin/tna-build .local/bin/tna-run
ENV PATH="$VIRTUAL_ENV/bin:/home/app/.local/bin:$PATH"

LABEL version="0.1.0"
EXPOSE 8080
