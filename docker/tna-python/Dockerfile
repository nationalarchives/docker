FROM python:3.11-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && \
    apt-get install -y --no-install-recommends gettext=0.21-12 curl=7.88.1-10 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd --create-home app
USER app
WORKDIR /home/app

ENV VIRTUAL_ENV=/opt/env
RUN python -m venv $VIRTUAL_ENV && \
    pip install --upgrade --no-cache-dir pip==23.1.2 gunicorn==21.1.0

COPY --chown=app bin/tna-build bin/tna-run .local/bin/
RUN chmod +x .local/bin/tna-build .local/bin/tna-run

# COPY --chown=app pyproject.toml.template ./

ENV PATH="/opt/env/bin:/home/app/.local/bin:$PATH"

LABEL version="0.1.0"
EXPOSE 8080
