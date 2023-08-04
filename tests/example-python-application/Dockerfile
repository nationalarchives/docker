FROM tna-python

# Copy in the pyproject.toml poetry.lock files
COPY --chown=app pyproject.toml poetry.lock ./

# Install the dependencies
RUN tna-build

# Copy in the rest of the application code
COPY --chown=app . .

# Run the application
CMD ["tna-run", "my-tna-app:app"]
