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
