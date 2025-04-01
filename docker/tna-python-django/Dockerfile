ARG BASE_IMAGE=ghcr.io/nationalarchives/tna-python
ARG BASE_IMAGE_TAG=latest

# wiz-scan ignore-line
FROM "$BASE_IMAGE":"$BASE_IMAGE_TAG"

# ==========================================
# Add some opencontainer labels which GitHub
# uses to display additional information
# ==========================================
ARG TNA_DOCKER_IMAGE_SOURCE
LABEL org.opencontainers.image.description="National Archives base Docker image" \
    org.opencontainers.image.source="$TNA_DOCKER_IMAGE_SOURCE" \
    org.opencontainers.image.licenses=MIT

# ==========================================
# Move the existing build and run scripts to
# a -common suffix so that we can keep using
# the base tna-build and tna-run commands
# ==========================================
RUN set -eux; \
    \
    mv /home/app/.local/bin/tna-build /home/app/.local/bin/tna-build-common; \
    mv /home/app/.local/bin/tna-run /home/app/.local/bin/tna-run-common

# ==========================================
# These new commands are just proxies to the
# renamed tna-build/tna-run scripts included
# in the parent Docker image, but with extra
# Django-specific commands
# ==========================================
# wiz-scan ignore-line
COPY --chown=app bin/tna-build bin/tna-run bin/manage /home/app/.local/bin/

# ==========================================
# manage.py is the recommended Django way of
# running administrative tasks, and while it
# might be replaced by the application, this
# way we can ensure running the Docker image
# should still still work albeit not with no
# output
# ==========================================
# wiz-scan ignore-line
COPY --chown=app lib/manage.py /app

# ==========================================
# Allow all our scripts to be executable
# ==========================================
RUN chmod +x /home/app/.local/bin/tna-build /home/app/.local/bin/tna-run /home/app/.local/bin/manage /home/app/.local/bin/migrate manage.py
