FROM tna-python

# Copy in the project Python dependency files
COPY --chown=app pyproject.toml poetry.lock ./
# Copy in the project Node dependency files
COPY --chown=app package.json package-lock.json .nvmrc ./

# Install the dependencies
RUN tna-build

# Copy in the rest of the application code
COPY --chown=app . .

# Run the application
CMD ["tna-run", "my_tna_app:app"]
