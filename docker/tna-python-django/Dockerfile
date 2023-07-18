FROM ghcr.io/nationalarchives/tna-python:latest

WORKDIR /home/app

COPY --chown=app bin/tna-run .local/bin/
RUN chmod +x .local/bin/tna-run

COPY --chown=app lib/manage.py .
# RUN chmod +x manage.py

# RUN echo "poetry add Django@4.2" >> .local/bin/tna-build
