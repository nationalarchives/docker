ARG BASE_IMAGE_TAG=latest
FROM ghcr.io/nationalarchives/tna-python:"$BASE_IMAGE_TAG"

# ==========================================
# Move the existing build and run scripts to
# a -common suffix so that we can keep using
# the base tna-build and tna-run commands
# ==========================================
RUN set -eux; \
    \
    mv /home/app/.local/bin/tna-run /home/app/.local/bin/tna-run-common

# ==========================================
# These new commands are just proxies to the
# renamed tna-build/tna-run scripts included
# in the parent Docker image, but with extra
# Django-specific commands
# ==========================================
COPY --chown=app bin/tna-run /home/app/.local/bin/

# ==========================================
# Allow all our scripts to be executable
# ==========================================
RUN chmod +x /home/app/.local/bin/tna-run
