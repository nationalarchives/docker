FROM python:3.14-slim-trixie

# ==========================================
# Label this container image with a semantic
# version number
# ==========================================
ARG TNA_DOCKER_IMAGE_VERSION
LABEL version="$TNA_DOCKER_IMAGE_VERSION"

# ==========================================
# Add some opencontainer labels which GitHub
# uses to display additional information
# ==========================================
ARG TNA_DOCKER_IMAGE_SOURCE
LABEL org.opencontainers.image.description="National Archives base Docker image" \
    org.opencontainers.image.source="$TNA_DOCKER_IMAGE_SOURCE" \
    org.opencontainers.image.licenses=MIT

# ==========================================
# All TNA containers SHOULD expose identical
# ports which will then be mapped to another
# port on the host system - we use a default
# of port 8080 for all our applications
# ==========================================
ENV PORT=8080
EXPOSE 8080/tcp

# ==========================================
# To aid consistency Dockerised applications
# should expose an unauthenticated URI which
# can be used as a healthcheck by Docker and
# other container orchestrators to check the
# alive-ness of an application which idea is
# based on a GOV.UK proposal:
# github.com/alphagov/govuk-rfcs/blob/main/rfc-141-application-healthchecks.md
# ==========================================
HEALTHCHECK CMD ALLOW_INSECURE="$(echo "${ALLOW_INSECURE:-'false'}" | tr '[:upper:]' '[:lower:]')" && HEALTHCHECK_PROTOCOL=$(if [ "$ALLOW_INSECURE" = 'true' ]; then echo 'http'; else echo 'https'; fi) && curl --fail --insecure "$HEALTHCHECK_PROTOCOL://localhost:$PORT/healthcheck/live/" || exit 1

# ==========================================
# Set Python up in a consistent manner, with
# things like ensuring no Python bytecode is
# written to ephemeral Docker instances, and
# allowing the output to be streamed up into
# the terminal of the host machine
# ==========================================
ENV PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random

# ==========================================
# We don't want to use a cache directory for
# pip and we can safely ignore the check for
# the pip version because the version of pip
# has been defined and installed in the base
# Python image
# ==========================================
ENV PIP_NO_CACHE_DIR=true \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# ==========================================
# Define the versions of packages to install
# at build - these are safe because:
#   "You can't override or set an
#    environment variable at build-time"
# > docs.docker.com/build/building/variables
# ==========================================
ENV POETRY_VERSION=2.2.1 \
    NVM_VERSION=0.40.3 \
    WSGI_GUNICORN_VERSION=23.0.0 \
    ASGI_UVICORN_VERSION=0.40.0

# ==========================================
# Create a new non-root level "app" user who
# owns a home directory where we can install
# our scripts and libraries into
# ==========================================
ARG USERNAME=app
ARG USER_UID=1001
ARG USER_GID="$USER_UID"
RUN groupadd --gid "$USER_GID" "$USERNAME" \
    && useradd --no-log-init --uid "$USER_UID" --gid "$USER_GID" --create-home "$USERNAME" --shell /bin/bash
ENV HOME="/home/$USERNAME"

# ==========================================
# Set up the Poetry variables so that we get
# a consistent experience with using Poetry,
# which includes where it will be installed,
# where it installs the project dependencies
# ==========================================
ENV POETRY_HOME="$HOME/.local" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=false
    
# ==========================================
# Specify the directory for nvm to use which
# is writable by our "app" user, and set the
# Node.js environment to "production"
# ==========================================
ENV NVM_DIR="$HOME/.nvm"
ENV NODE_ENV=production

# ==========================================
# Ensure the `/bin/sh -c` interpreter Docker
# executes commands through doesn't just use
# the final operation in a pipe to determine
# the success of the entire command
# > github.com/hadolint/hadolint/wiki/DL4006
# ==========================================
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# ==========================================
# Update the package index files and install
# specific versions of libcurl4, curl, build
# essentials (which then enables us to later
# install Poetry) after which go on to clean
# and remove all the apt registries to avoid
# the possibility of additional applications
# being installed later on
# ==========================================
RUN set -eux; \
    export DEBIAN_FRONTEND=noninteractive; \
    apt-get update; \
    apt-get -y upgrade; \
    apt-get install -y --no-install-recommends curl=8.14.1-2+deb13u2; \
    apt-get clean; \
    apt-get autoremove -y --purge; \
	rm -rfv /var/lib/apt/lists/*

# ==========================================
# Upgrade pip to a later version
# ==========================================
RUN pip install --no-cache-dir --quiet --upgrade pip==25.3

# ==========================================
# Create an "/app" directory in the root dir
# for the application code and allow the new
# app user to access it
# ==========================================
RUN mkdir -p /app; \
    chown "${USER_UID}":"${USER_GID}" -R /app; \
    chmod 700 /app

# ==========================================
# Install Poetry in the suggested manner and
# nvm so we can build static assets like CSS
# and JavaScript
# ==========================================
RUN set -eux; \
    curl -sSL "https://install.python-poetry.org" | python -; \
    curl -o- "https://raw.githubusercontent.com/nvm-sh/nvm/v$NVM_VERSION/install.sh" | bash; \
    chown app:app -R "$POETRY_HOME" "$NVM_DIR"

# ==========================================
# Remove some vulnerable and unused packages
# to reduce the potential attack surface
# ==========================================
RUN apt-get remove --purge -y --allow-remove-essential mount util-linux login.defs login:arm64; \
    apt-get clean; \
    apt-get autoremove -y --purge

# ==========================================
# Change the image current working directory
# to the new /app directory we just created,
# ready for our application code
# ==========================================
WORKDIR /app

# ==========================================
# Add the Poetry binary to our path
# ==========================================
ENV PATH="$POETRY_HOME/bin:$PATH"

# ==========================================
# Now we have finished installing everything
# at a system level, change the current user
# to the non-root user we created previously
# to avoid any bad actors gaining root level
# permissions
# ==========================================
USER app

# ==========================================
# Install the latest LTS version of Node.js,
# but keeping within the releases code-named
# "krypton" (v24.x)
# ==========================================
# hadolint ignore=SC1091
RUN . "$NVM_DIR/nvm.sh"; \
    nvm install --latest-npm lts/krypton; \
    nvm alias default lts/krypton

# ==========================================
# Create a directory for our SSL certificate
# files
# ==========================================
RUN mkdir /home/app/ssl

# ==========================================
# Into our .local/bin/ directory copy in the
# bash scripts we need in order to build and
# run our application in a consistent manner
# ==========================================
COPY bin /home/app/.local/bin

# ==========================================
# This does nothing but will act as a way to
# stop the container from shutting down once
# it has been booted which then allows us to
# run, inspect and debug the container, even
# though we have no application running
# ==========================================
CMD ["tail", "-f", "/dev/null"]
