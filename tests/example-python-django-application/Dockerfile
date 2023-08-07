FROM tna-python-django

# Copy in the project Python dependency files
COPY --chown=app pyproject.toml poetry.lock ./

# Install the dependencies
RUN tna-build-django

# Copy in the rest of the application code
COPY --chown=app . .

# Run the application
CMD ["tna-run-django", "my_tna_app.wsgi:application"]
