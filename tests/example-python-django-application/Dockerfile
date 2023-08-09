FROM tna-python-django

# Copy in the rest of the application code
COPY --chown=app . .

# Install the dependencies
RUN tna-build

# Run the application
CMD ["tna-run", "my_tna_app.wsgi:application"]
