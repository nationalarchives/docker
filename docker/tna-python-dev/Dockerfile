# wiz-scan ignore
ARG BASE_IMAGE=ghcr.io/nationalarchives/tna-python
ARG BASE_IMAGE_TAG=latest

FROM "$BASE_IMAGE":"$BASE_IMAGE_TAG"

# ARG TARGETPLATFORM  # linux/amd64 or linux/arm64

# ==========================================
# This is already defined in the base image,
# but we redefine it here as HTTP because an
# application might be using HTTPS
# ==========================================
HEALTHCHECK CMD curl --fail "http://localhost:$APPLICATION_PORT/healthcheck/live/" || exit 1

# ==========================================
# Ensure the `/bin/sh -c` interpreter Docker
# executes commands through doesn't just use
# the final operation in a pipe to determine
# the success of the entire command
# https://github.com/hadolint/hadolint/wiki/DL4006
# ==========================================
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# ==========================================
# Switch back to the root user so we can run
# commands that need elevated privileges and
# not encounter permission issues when using
# files and directories from the host system
# which are mounted during development
# ==========================================
USER root

# ==========================================
# Update the package index files and install
# git, removing any unnecessary packages
# ==========================================
RUN apt-get update; \
    apt-get install -y --no-install-recommends git=1:2.47.3-0+deb13u1; \
    apt-get clean; \
    apt-get autoremove -y --purge; \
	rm -rfv /var/lib/apt/lists/*

# ==========================================
# Set the versions for various tools that we
# want to install to help with development
# ==========================================
ENV RUFF_VERSION=0.15.13 \
    DJLINT_VERSION=1.36.4 \
    DJHTML_VERSION=3.0.11 \
    DJANGO_DEBUG_TOOLBAR_VERSION=6.3.0 \
    PRETTIER_VERSION=3.8.3 \
    STYLELINT_VERSION=17.11.0 \
    STYLELINT_CONFIG_STANDARD_SCSS_VERSION=17.0.0 \
    STYLELINT_ORDER_VERSION=8.1.1 \
    STYLELINT_SELECTOR_BEM_PATTERN_VERSION=4.0.1 \
    STYLELINT_ORDER_VERSION=8.1.1

# ==========================================
# Create container labels containing version
# numbers for the software we have installed
# in this image
# ==========================================
LABEL uk.gov.nationalarchives.ruff-version="$RUFF_VERSION"
LABEL uk.gov.nationalarchives.djlint-version="$DJLINT_VERSION"
LABEL uk.gov.nationalarchives.djhtml-version="$DJHTML_VERSION"
LABEL uk.gov.nationalarchives.django-debug-toolbar-version="$DJANGO_DEBUG_TOOLBAR_VERSION"
LABEL uk.gov.nationalarchives.prettier-version="$PRETTIER_VERSION"
LABEL uk.gov.nationalarchives.stylelint-version="$STYLELINT_VERSION"
LABEL uk.gov.nationalarchives.stylelint-config-standard-scss-version="$STYLELINT_CONFIG_STANDARD_SCSS_VERSION"
LABEL uk.gov.nationalarchives.stylelint-selector-bem-pattern-version="$STYLELINT_SELECTOR_BEM_PATTERN_VERSION"
LABEL uk.gov.nationalarchives.stylelint-order-version="$STYLELINT_ORDER_VERSION"
    
# ==========================================
# Set the Node.js environment to development
# ==========================================
ENV NODE_ENV=development

# ==========================================
# Set the default log level for applications
# running in development to "debug"
# ==========================================
ENV LOG_LEVEL=debug

# ==========================================
# Set the location of the Ruff cache outside
# the project root
# ==========================================
ENV RUFF_CACHE_DIR=/home/app/.ruff_cache

# ==========================================
# Install the tools required for linting and
# fixing Python, HTML, CSS and JavaScript
# ==========================================
# hadolint ignore=SC1091
RUN . tna-nvm; \
    nvm use default; \
    npm config set fund=false --location=global; \
    npm install --global --silent --save-exact "prettier@$PRETTIER_VERSION" "stylelint@$STYLELINT_VERSION" "stylelint-config-standard-scss@$STYLELINT_CONFIG_STANDARD_SCSS_VERSION" "stylelint-order@$STYLELINT_ORDER_VERSION" "stylelint-selector-bem-pattern@$STYLELINT_SELECTOR_BEM_PATTERN_VERSION" "stylelint-order@$STYLELINT_ORDER_VERSION" @nationalarchives/eslint-config@latest @nationalarchives/frontend@latest; \
    python -m pip install --no-cache-dir --quiet ruff=="$RUFF_VERSION" djlint=="$DJLINT_VERSION" djhtml=="$DJHTML_VERSION"

# ==========================================
# Copy the development scripts into the user
# .local/bin/dev/ directory, and prepare the
# future .local/bin/tasks/ directory, adding
# it to the path ready for mounted scripts
# ==========================================
COPY bin/dev /home/app/.local/bin/dev
RUN chmod +x -R /home/app/.local/bin/dev
ENV PATH="/home/app/.local/bin/tasks:/home/app/.local/bin/dev:$PATH"

# ==========================================
# Copy all configuration files into the main
# app directory
# ==========================================
COPY lib/* /home/app/

# ==========================================
# Update the build and run scripts with some
# development specific versions
# ==========================================
RUN set -eux; \
    mv /home/app/.local/bin/tna-build /home/app/.local/bin/tna-build-base
COPY bin/tna-asgi /home/app/.local/bin/tna-asgi
COPY bin/tna-build /home/app/.local/bin/tna-build
COPY bin/tna-clean /home/app/.local/bin/tna-clean
COPY bin/tna-wsgi /home/app/.local/bin/tna-wsgi
