# https://hub.docker.com/_/debian/tags?page=1&name=bookworm-slim
# https://hub.docker.com/_/python/tags?page=1&name=3.11-slim
FROM python:3.11-slim

ARG TNA_DOCKER_IMAGE_VERSION
LABEL version="${TNA_DOCKER_IMAGE_VERSION}" \
    org.opencontainers.image.description="National Archives base Docker image"
EXPOSE 8080/tcp
HEALTHCHECK CMD curl --fail http://localhost:8080/healthcheck/ || exit 1

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    ENVIRONMENT=production \
    POETRY_HOME=/home/app/.local \
    POETRY_VERSION=1.5.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN set -eux; \
    \
	savedAptMark="$(apt-mark showmanual)"; \
    \
    apt-get update; \
    apt-get install -y --no-install-recommends curl; \
    \
    useradd --system --create-home app; \
    \
    mkdir -p /app; \
    chown app:app -R /app; \
    chmod 700 /app

# ==========================================
# Fix for CVE-2022-40897

ENV PYTHON_PIP_VERSION 23.1.2
ENV PYTHON_SETUPTOOLS_VERSION 68.0.0

# https://github.com/pypa/get-pip
ENV PYTHON_GET_PIP_URL https://github.com/pypa/get-pip/raw/9af82b715db434abb94a0a6f3569f43e72157346/public/get-pip.py
ENV PYTHON_GET_PIP_SHA256 45a2bb8bf2bb5eff16fdd00faef6f29731831c7c59bd9fc2bf1f3bed511ff1fe

RUN set -eux; \
	\
	savedAptMark="$(apt-mark showmanual)"; \
	apt-get update; \
	apt-get install -y --no-install-recommends wget; \
	\
	wget -O get-pip.py "$PYTHON_GET_PIP_URL"; \
	echo "$PYTHON_GET_PIP_SHA256 *get-pip.py" | sha256sum -c -; \
	\
	apt-mark auto '.*' > /dev/null; \
	[ -z "$savedAptMark" ] || apt-mark manual $savedAptMark > /dev/null; \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	\
	python get-pip.py \
		--disable-pip-version-check \
		--no-cache-dir \
		--no-compile \
		"pip==$PYTHON_PIP_VERSION" \
		"setuptools==$PYTHON_SETUPTOOLS_VERSION" \
	; \
	rm -f get-pip.py; \
	\
	pip --version
# End fix
# ==========================================

WORKDIR /app

RUN curl -sSL "https://install.python-poetry.org" | python -;

ENV PATH="$POETRY_HOME/bin:$PATH"

# RUN set -eux; \
#     \
#     apt-get remove -y curl wget; \
#     apt-get clean; \
#     apt-get autoremove -y --purge; \
# 	rm -rf /var/lib/apt/lists/*

USER app

COPY --chown=app bin/tna-build bin/tna-run /home/app/.local/bin/
RUN chmod +x /home/app/.local/bin/tna-build /home/app/.local/bin/tna-run

# CMD tail -f /dev/null
