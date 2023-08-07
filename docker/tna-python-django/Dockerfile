# TODO: Change to latest
FROM ghcr.io/nationalarchives/tna-python:0.1.2

# ==========================================
# These "-django" suffixed commands are just
# proxies to the inherited tna-build/tna-run
# scripts that were copied in the tna-python
# Docker image, but with some extra commands
# that are specific to Django
# ==========================================
COPY --chown=app bin/tna-build-django bin/tna-run-django $HOME/.local/bin/
RUN chmod +x /home/app/.local/bin/tna-build-django /home/app/.local/bin/tna-run-django

# ==========================================
# manage.py is the recommended Django way of
# running administrative tasks, and while it
# might be replaced by the application, this
# way we can ensure running the Docker image
# should still still work albeit not with no
# output
# ==========================================
COPY --chown=app lib/manage.py /app
RUN chmod +x manage.py
