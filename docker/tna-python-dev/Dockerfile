# wiz-scan ignore
ARG BASE_IMAGE=ghcr.io/nationalarchives/tna-python
ARG BASE_IMAGE_TAG=latest

FROM "$BASE_IMAGE":"$BASE_IMAGE_TAG"

# ARG TARGETPLATFORM  # linux/amd64 or linux/arm64

# ==========================================
# This is already defined in the base image,
# but we set it again to avoid Wiz reporting
# errors with a missing healthcheck
# ==========================================
HEALTHCHECK CMD curl --fail "http://localhost:$PORT/healthcheck/live/" || exit 1

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
ENV BLACK_VERSION=25.12.0 \
    FLAKE8_VERSION=7.1.1 \
    ISORT_VERSION=7.0.0 \
    DJLINT_VERSION=1.36.4 \
    DJHTML_VERSION=3.0.10 \
    DJANGO_DEBUG_TOOLBAR_VERSION=6.1.0 \
    PRETTIER_VERSION=3.7.4 \
    STYLELINT_VERSION=17.0.0 \
    STYLELINT_CONFIG_STANDARD_SCSS_VERSION=16.0.0 \
    STYLELINT_SELECTOR_BEM_PATTERN_VERSION=4.0.1 \
    STYLELINT_ORDER_VERSION=7.0.1 \
    ESLINT_VERSION=8.56.0
    
# ==========================================
# Set the Node.js environment to development
# ==========================================
ENV NODE_ENV=development

# ==========================================
# Install the tools required for linting and
# fixing Python
# ==========================================
RUN python -m pip install --no-cache-dir --quiet black=="$BLACK_VERSION" flake8=="$FLAKE8_VERSION" isort=="$ISORT_VERSION" djlint=="$DJLINT_VERSION" djhtml=="$DJHTML_VERSION"

# ==========================================
# Copy any configuration files into the main
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

# ==========================================
# Copy the development scripts into the user
# .local/bin/dev/ directory, and prepare the
# future .local/bin/tasks/ directory, adding
# it to the path ready for mounted scripts
# ==========================================
COPY bin/dev /home/app/.local/bin/dev
RUN chmod +x -R /home/app/.local/bin/dev
ENV PATH="/home/app/.local/bin/tasks:/home/app/.local/bin/dev:$PATH"
