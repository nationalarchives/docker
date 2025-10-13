ARG BASE_IMAGE=ghcr.io/nationalarchives/tna-python
ARG BASE_IMAGE_TAG=latest

# wiz-scan ignore-line
FROM "$BASE_IMAGE":"$BASE_IMAGE_TAG"

# ==========================================
# Add some opencontainer labels which GitHub
# uses to display additional information
# ==========================================
ARG TNA_DOCKER_IMAGE_SOURCE
# LABEL org.opencontainers.image.description="National Archives base Docker image" \
#     org.opencontainers.image.source="$TNA_DOCKER_IMAGE_SOURCE" \
#     org.opencontainers.image.licenses=MIT
LABEL org.opencontainers.image.source="$TNA_DOCKER_IMAGE_SOURCE"

# ==========================================
# Move the existing build and run scripts to
# a -common suffix so that we can keep using
# the base tna-build and tna-run commands
# ==========================================
RUN set -eux; \
    mv /home/app/.local/bin/tna-build /home/app/.local/bin/tna-build-common

# ==========================================
# Copy in Django specific scripts
# ==========================================
# wiz-scan ignore-line
COPY --chown=app bin/tna-build bin/manage /home/app/.local/bin/

# ==========================================
# Allow all our scripts to be executable
# ==========================================
RUN chmod +x /home/app/.local/bin/tna-build /home/app/.local/bin/manage
