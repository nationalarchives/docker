# wiz-scan ignore
ARG BASE_IMAGE=ghcr.io/nationalarchives/tna-python-root
ARG BASE_IMAGE_TAG=latest

ARG TARGETPLATFORM

FROM "$BASE_IMAGE":"$BASE_IMAGE_TAG"

# ==========================================
# Ensure the `/bin/sh -c` interpreter Docker
# executes commands through doesn't just use
# the final operation in a pipe to determine
# the success of the entire command
# https://github.com/hadolint/hadolint/wiki/DL4006
# ==========================================
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# ==========================================
# Check for the existance of a file that has
# been created by the container after it has
# finished installing and configuring itself
# ==========================================
HEALTHCHECK --interval=10s CMD test -f /tmp/up

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
    apt-get install -y --no-install-recommends docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin; \
    \
    apt-get clean; \
    apt-get autoremove -y --purge; \
    rm -rfv /var/lib/apt/lists/*

# ==========================================
# Install the AWS CLI
# ==========================================
COPY lib/aws-cli-public.key /home/app/aws-cli-public.key

ENV AWS_CLI_VERSION=2.27.28

RUN [[ "$TARGETPLATFORM" == "linux/arm64" ]] && curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64-$AWS_CLI_VERSION.zip" -o awscliv2.zip || curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-$AWS_CLI_VERSION.zip" -o awscliv2.zip; \
    gpg --import /home/app/aws-cli-public.key; \
    [[ "$TARGETPLATFORM" == "linux/arm64" ]] && curl -o awscliv2.sig "https://awscli.amazonaws.com/awscli-exe-linux-aarch64-$AWS_CLI_VERSION.zip.sig" || curl -o awscliv2.sig "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-$AWS_CLI_VERSION.zip.sig"; \
    gpg --verify awscliv2.sig awscliv2.zip; \
    unzip awscliv2.zip; \
    ls -alh aws; \
    ./aws/install; \
    rm -fR awscliv2.zip awscliv2.sig aws

# ==========================================
# Copy the development scripts into the user
# .local/bin/dev/ directory, and prepare the
# future .local/bin/tasks/ directory, adding
# it to the path ready for mounted scripts
# ==========================================
COPY --chown=app bin /home/app/.local/bin/dev
RUN chmod +x -R /home/app/.local/bin/dev
ENV PATH="/home/app/.local/bin/tasks:/home/app/.local/bin/dev:$PATH"

# ==========================================
# Copy any configuration files into the main
# app directory
# ==========================================
COPY --chown=app lib/* /home/app/

# ==========================================
# Install the tools required for linting and
# fixing Python
# ==========================================
RUN python -m pip install --no-cache-dir --quiet black==25.1.0 flake8==7.1.1 isort==6.0.1

CMD ["dev"]
