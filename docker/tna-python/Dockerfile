FROM python:3.11-slim

ARG TNA_DOCKER_IMAGE_VERSION
LABEL version="${TNA_DOCKER_IMAGE_VERSION}" \
    org.opencontainers.image.description="National Archives base Docker image"
EXPOSE 8080/tcp
HEALTHCHECK CMD curl --fail http://localhost:8080/healthcheck/ || exit 1

ENV ENVIRONMENT=production \
    PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=true \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_HOME=/home/app/.local \
    POETRY_VERSION=1.5.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=false

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN set -eux; \
    \
    apt-get update; \
    apt-get install -y --no-install-recommends curl=7.88.1-10+deb12u1; \
    apt-get clean; \
    apt-get autoremove -y --purge; \
	rm -rf /var/lib/apt/lists/*; \
    \
    useradd --system --create-home app; \
    \
    mkdir -p /app; \
    chown app:app -R /app; \
    chmod 700 /app

WORKDIR /app

RUN set -eux; \
    \
    curl -sSL "https://install.python-poetry.org" | python -; \
    apt-get remove --purge -y curl;

ENV PATH="$POETRY_HOME/bin:$PATH"

# ==========================================
# Fix for CVE-2022-40897
# https://access.redhat.com/security/cve/cve-2022-40897
RUN rm -fR $POETRY_HOME/venv/lib/python3.11/site-packages/setuptools-65.5.0.dist-info
# ==========================================

USER app

COPY --chown=app bin/tna-build bin/tna-run /home/app/.local/bin/
RUN chmod +x /home/app/.local/bin/tna-build /home/app/.local/bin/tna-run

# CMD tail -f /dev/null
