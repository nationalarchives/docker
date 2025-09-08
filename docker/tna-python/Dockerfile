ARG USER_IMAGE=app

FROM python:3.13-slim-bookworm AS root

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
# All TNA containers should expose identical
# ports which will then be mapped to another
# port on the host system - we use port 8080
# for all our applications
# ==========================================
EXPOSE 8080/tcp

# ==========================================
# To aid consistency Dockerised applications
# should expose an unauthenticated URI which
# can be used as a healthcheck by Docker and
# other container orchestrators to check the
# live-ness of an application - this idea is
# based on a GOV.UK proposal:
# https://github.com/alphagov/govuk-rfcs/blob/main/rfc-141-application-healthchecks.md
# ==========================================
HEALTHCHECK --interval=15s CMD curl --fail http://localhost:8080/healthcheck/live/ || exit 1

# ==========================================
# The default runtime option is "production"
# with the only other option being "develop"
# which ensures all our production instances
# will act in a similar manner, and have the
# same setup and configuration
# ==========================================
ENV RUNTIME=production

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
# Set up the Poetry variables so that we get
# a consistent experience with using Poetry,
# which includes where it will be installed,
# where it installs the project dependencies
# and what version is used
# ==========================================
ENV POETRY_HOME=/home/app/.local \
    POETRY_VERSION=2.1.4 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=false

# ==========================================
# Ensure the `/bin/sh -c` interpreter Docker
# executes commands through doesn't just use
# the final operation in a pipe to determine
# the success of the entire command
# https://github.com/hadolint/hadolint/wiki/DL4006
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
    \
    export DEBIAN_FRONTEND=noninteractive; \
    \
    apt-get update; \
    apt-get -y upgrade; \
    apt-get install -y --no-install-recommends libcurl4=7.88.1-10+deb12u12 curl=7.88.1-10+deb12u12 build-essential=12.9 libmagic-dev=1:5.44-3 libsqlite3-0=3.40.1-2+deb12u2; \
    \
    apt-get clean; \
    apt-get autoremove -y --purge; \
	rm -rfv /var/lib/apt/lists/*

# ==========================================
# Create a new system-level nonroot user who
# owns a home directory where we can install
# libraries into (along with our scripts for
# building and running)
# ==========================================
RUN useradd --system --create-home app

# ==========================================
# Create an "/app" directory in the root dir
# for the application code and allow the new
# app user to access it
# ==========================================
RUN mkdir -p /app; \
    chown app:app -R /app; \
    chmod 700 /app

# ==========================================
# Set $HOME env var to be the home directory
# of our new app user so we can install libs
# to that location
# ==========================================
ENV HOME=/home/app

# ==========================================
# Specify the directory for nvm to use which
# is writable by our "app" user
# ==========================================
ENV NVM_DIR="$HOME/.nvm"

# ==========================================
# Install Poetry in the suggested manner and
# nvm so we can build static assets like CSS
# and JavaScript
# ==========================================
RUN set -eux; \
    \
    curl -sSL "https://install.python-poetry.org" | python -; \
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash; \
    chown app:app -R "$POETRY_HOME" "$NVM_DIR"

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



FROM root AS app
# ==========================================
# Now we have finished installing everything
# at a system level, change the current user
# to the non-root user we created previously
# to avoid any bad actors gaining root level
# permissions
# ==========================================
USER app



# wiz-scan ignore-block
# hadolint ignore=DL3006
FROM "$USER_IMAGE"

# ==========================================
# Install the latest LTS version of Node.js,
# but keeping within the releases code-named
# "jod" (v22.x)
# ==========================================
# hadolint ignore=SC1091
RUN . "$NVM_DIR/nvm.sh"; \
    nvm install lts/jod; \
    nvm alias default lts/jod

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
# wiz-scan ignore-line
COPY --chown=app bin /home/app/.local/bin
RUN chmod +x -fR /home/app/.local/bin

# ==========================================
# This does nothing but will act as a way to
# stop the container from shutting down once
# it has been booted which then allows us to
# run, inspect and debug the container, even
# though we have no application running
# ==========================================
CMD ["tail", "-f", "/dev/null"]
