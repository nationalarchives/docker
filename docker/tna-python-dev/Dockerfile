ARG BASE_IMAGE=ghcr.io/nationalarchives/tna-python-root
ARG BASE_IMAGE_TAG=latest

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
# Install and configure Docker, removing all
# lists afterwards
# ==========================================
RUN apt-get update; \
    apt-get install -y --no-install-recommends ca-certificates=20230311 gnupg=2.2.40-1.1; \
    install -m 0755 -d /etc/apt/keyrings; \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg; \
    chmod a+r /etc/apt/keyrings/docker.gpg; \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null; \
    apt-get update; \
    apt-get install -y --no-install-recommends docker-ce=5:27.3.1-1~debian.12~bookworm docker-ce-cli=5:27.3.1-1~debian.12~bookworm containerd.io=1.7.23-1 docker-buildx-plugin=0.17.1-1~debian.12~bookworm docker-compose-plugin=2.29.7-1~debian.12~bookworm; \
    apt-get clean; \
    apt-get autoremove -y --purge; \
    rm -rfv /var/lib/apt/lists/*

# ==========================================
# Copy the development scripts into the user
# .local/bin/dev/ directory
# ==========================================
COPY --chown=app bin /home/app/.local/bin/dev
RUN chmod +x -fR /home/app/.local/bin/dev
ENV PATH="/home/app/.local/bin/dev:$PATH"

# ==========================================
# Copy any configuration files into the main
# app directory
# ==========================================
COPY --chown=app lib/* /home/app/

CMD ["dev"]
