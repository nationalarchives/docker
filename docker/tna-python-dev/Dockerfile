# wiz-scan ignore
ARG BASE_IMAGE=ghcr.io/nationalarchives/tna-python
ARG BASE_IMAGE_TAG=latest

FROM "$BASE_IMAGE":"$BASE_IMAGE_TAG"

ARG TARGETPLATFORM

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
# Install and configure Docker, removing all
# lists afterwards
# ==========================================
RUN apt-get update; \
    apt-get install -y --no-install-recommends gnupg git unzip; \
    install -m 0755 -d /etc/apt/keyrings; \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg; \
    chmod a+r /etc/apt/keyrings/docker.gpg; \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null; \
    apt-get update; \
    apt-get install -y --no-install-recommends docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin postgresql-client; \
    apt-get clean; \
    apt-get autoremove -y --purge; \
    rm -rfv /var/lib/apt/lists/*

# ==========================================
# Set versions for tools we want to install
# ==========================================
ENV AWS_CLI_VERSION=2.27.45 \
    BLACK_VERSION=25.9.0 \
    FLAKE8_VERSION=7.1.1 \
    ISORT_VERSION=7.0.0 \
    PRETTIER_VERSION=3.6.2 \
    STYLELINT_VERSION=16.25.0 \
    STYLELINT_CONFIG_STANDARD_SCSS_VERSION=16.0.0 \
    STYLELINT_SELECTOR_BEM_PATTERN_VERSION=4.0.1 \
    STYLELINT_ORDER_VERSION=7.0.0 \
    ESLINT_VERSION=8.56.0

# ==========================================
# Install the AWS CLI
# ==========================================
COPY lib/aws-cli-public.key /home/app/aws-cli-public.key
RUN gpg --import /home/app/aws-cli-public.key; \
    AWS_CLI_PLATFORM=none; \
    [[ "$TARGETPLATFORM" == "linux/amd64" ]] && AWS_CLI_PLATFORM=x86_64; \
    [[ "$TARGETPLATFORM" == "linux/arm64" ]] && AWS_CLI_PLATFORM=aarch64; \
    echo "Downloading AWS CLI v$AWS_CLI_VERSION for $TARGETPLATFORM using $AWS_CLI_PLATFORM..."; \
    curl -o /home/app/awscliv2.zip "https://awscli.amazonaws.com/awscli-exe-linux-$AWS_CLI_PLATFORM-$AWS_CLI_VERSION.zip"; \
    curl -o /home/app/awscliv2.zip.sig "https://awscli.amazonaws.com/awscli-exe-linux-$AWS_CLI_PLATFORM-$AWS_CLI_VERSION.zip.sig"; \
    gpg --verify /home/app/awscliv2.zip.sig /home/app/awscliv2.zip; \
    unzip /home/app/awscliv2.zip; \
    ./aws/install -i /usr/local/aws-cli -b /usr/local/bin; \
    rm -fR /home/app/awscliv2.zip /home/app/awscliv2.zip.sig /home/app/aws

# ==========================================
# Install the tools required for linting and
# fixing Python
# ==========================================
RUN python -m pip install --no-cache-dir --quiet black=="$BLACK_VERSION" flake8=="$FLAKE8_VERSION" isort=="$ISORT_VERSION"

# ==========================================
# Copy any configuration files into the main
# app directory
# ==========================================
COPY --chown=app lib/* /home/app/

# ==========================================
# Update the build and run scripts with some
# development specific versions
# ==========================================
RUN set -eux; \
    mv /home/app/.local/bin/tna-build /home/app/.local/bin/tna-build-common
COPY --chown=app bin/tna-build /home/app/.local/bin/tna-build
COPY --chown=app bin/tna-build-dev /home/app/.local/bin/tna-build-dev
COPY --chown=app bin/tna-run /home/app/.local/bin/tna-run

# ==========================================
# Copy the development scripts into the user
# .local/bin/dev/ directory, and prepare the
# future .local/bin/tasks/ directory, adding
# it to the path ready for mounted scripts
# ==========================================
COPY --chown=app bin/dev /home/app/.local/bin/dev
RUN chmod +x -R /home/app/.local/bin/dev
ENV PATH="/home/app/.local/bin/tasks:/home/app/.local/bin/dev:$PATH"
