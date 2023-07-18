FROM ghcr.io/nationalarchives/tna-python:latest

COPY --chown=app:app bin/tna-run .local/bin/
RUN chmod +x .local/bin/tna-run

COPY --chown=app:app lib/manage.py .
# RUN chmod +x manage.py

RUN echo "poetry add Django@4.2" >> .local/bin/tna-build
