# tna-python

This Docker image:

- defines the version of Python used for all derivative images
- declares an open port
- creates a non-root user to execute the application with
- upgades pip
- copies the default build and run scripts

The dependencies declared are minimal and easy to maintain:

- gunicorn - so all Python applications can consistently be served behind a WSGI

## Environment variables

- `ENVIRONMENT` (default: `production`)

## Future

We could look at enforcing MKDocs as part of all Python projects to promote more documentation.
