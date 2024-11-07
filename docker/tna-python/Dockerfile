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
# port on the host system - we are using 443
# which is the standard port for HTTPS
# ==========================================
EXPOSE 443/tcp

# ==========================================
# To aid consistency Dockerised applications
# should expose an unauthenticated URI which
# can be used as a healthcheck by Docker and
# other container orchestrators to check the
# live-ness of an application - this idea is
# based on a GOV.UK proposal:
# https://github.com/alphagov/govuk-rfcs/blob/main/rfc-141-application-healthchecks.md
# This goes directly to the app, rather than
# through nginx
# ==========================================
HEALTHCHECK CMD curl --fail http://localhost:8080/healthcheck/live/ || exit 1

# ==========================================
# The default environment type is production
# and something different, like "develop" or
# "staging" will have to be given for others
# which provides us a failsafe to ensure the
# all our production instances will act in a
# similar way and have the same log level
# ==========================================
ENV ENVIRONMENT=production

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
    POETRY_VERSION=1.8.4 \
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
# 1.
# Update the package index files and install
# specific versions of libcurl4, curl, build
# essentials (which then enables us to later
# install Poetry), as well as both nginx and
# ufw - after this, clean and remove all the
# apt registries to avoid the possibility of
# additional installations later on
# ==========================================
RUN set -eux; \
    \
    export DEBIAN_FRONTEND=noninteractive; \
    \
    apt-get update; \
    apt-get -y upgrade; \
    apt-get install -y --no-install-recommends libcurl4=7.88.1-10+deb12u7 curl=7.88.1-10+deb12u7 build-essential=12.9 libmagic-dev=1:5.44-3 nginx=1.22.1-9 nginx-common=1.22.1-9 ufw=0.36.2-1 iptables=1.8.9-2; \
    \
    apt-get clean; \
    apt-get autoremove -y --purge; \
	rm -rfv /var/lib/apt/lists/*

# ==========================================
# Update the firewall rule to allow only for
# HTTPS, then create an SSL certificate that
# we can use locally in nginx to secure this
# container
# ==========================================
RUN ufw allow 'Nginx HTTPS'; \
    rm /etc/nginx/conf.d/default.conf; \
    mkdir /etc/nginx/ssl; \
    openssl req -x509 -noenc -newkey rsa:2048 -keyout /etc/nginx/ssl/key.pem -out /etc/nginx/ssl/req.pem -days 90 -subj "/C=GB/ST=London/L=Kew/O=The National Archives/OU=Digital/CN=localhost"

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
# Copy in the nginx configuration file which
# allows us to use a reverse proxy and serve
# the app securely through HTTPS
# ==========================================
COPY lib/nginx.conf /etc/nginx/nginx.conf

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
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash; \
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



FROM "$USER_IMAGE"

# ==========================================
# Install the latest LTS version of Node.js,
# but keeping within the releases code-named
# "jod" (v22.x)
# (Install the previous LTS release, just in
# case some applicaitons still use it)
# ==========================================
RUN . "$NVM_DIR/nvm.sh"; \
    nvm install lts/iron; \
    nvm install lts/jod; \
    nvm alias default lts/jod

# ==========================================
# Into our .local/bin/ directory copy in the
# bash scripts we need in order to build and
# run our application in a consistent manner
# ==========================================
COPY --chown=app bin/tna-build bin/tna-node bin/tna-run /home/app/.local/bin/
RUN chmod +x /home/app/.local/bin/tna-build /home/app/.local/bin/tna-node /home/app/.local/bin/tna-run

# ==========================================
# This does nothing but will act as a way to
# stop the container from shutting down once
# it has been booted which then allows us to
# run, inspect and debug the container, even
# though we have no application running
# ==========================================
CMD ["tail", "-f", "/dev/null"]
