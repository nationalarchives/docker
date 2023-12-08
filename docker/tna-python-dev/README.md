# tna-python-dev

This image extends `tna-python` but adds:

- `docker` - for managing other containers
- `black`, `flake8` and `isort` - for formatting Python code
- `prettier`, `eslint` and `stylelint` - for formatting JavaScript and CSS

## Environment variables

All environment variables defined in [tna-python](../tna-python/README.md).

## Commands for the Dockerfile

Run `help` from within the container to see a list of available commands.

### `format`

1. Run `isort`
1. Run `black`
1. Run `flake8`
1. Apply prettier to all files in the `/app` directory
1. Run `stylelint` against all SCSS files in the `/app` directory
1. Run `eslint` against all JavaScript files in the `/app` directory

### `upgrade`

1. Updates Poetry dependencies
1. Updates npm dependencies

### `secret-key`

Generate a string that can be used as the environment variable `SECRET_KEY`:

- https://docs.python.org/3/library/secrets.html
- https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
- https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY
