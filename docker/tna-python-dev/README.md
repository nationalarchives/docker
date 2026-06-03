# tna-python-dev

> ⚠️ Do not use `tna-python-dev` in production

This image extends `tna-python` and can be used for local development **ONLY**. It adds:

- `ruff` for formatting and linting Python
- `stylelint` and `eslint` for linting JavaScript and CSS
- `prettier` for formatting JavaScript, CSS, JSON, YAML etc.
- scripts for formatting
- `django-debug-toolbar` for debugging Django applications
- `git`

## Environment variables

All environment variables extended from [tna-python](../tna-python/README.md) but with some different defaults:

| Variable                   | Default                 |
| -------------------------- | ----------------------- |
| `LOG_LEVEL`                | `debug`                 |
| `NODE_ENV`                 | `development`           |
| `WORKERS`                  | _ignored_               |
| `THREADS`                  | _ignored_               |
| `TIMEOUT`                  | _ignored_               |
| `KEEP_ALIVE`               | _ignored_               |
| `APPLICATION_PROTOCOL`     | _ignored_ (`http` only) |
| `SSL_KEY_FILE`             | _ignored_               |
| `SSL_CERTIFICATE_FILE`     | _ignored_               |
| `SSL_CA_CERTIFICATES_FILE` | _ignored_               |
| `SSL_DOMAIN`               | _ignored_               |

### `tna-python-dev` specific

| Variable              | Description                                                | Default |
| --------------------- | ---------------------------------------------------------- | ------- |
| `NPM_DEVELOP_COMMAND` | The npm script from `package.json` to run while developing | _none_  |

## Using `tna-python-dev`

Assuming you are using the `tna-python` image in your `Dockerfile` like so:

```Dockerfile
ARG IMAGE=ghcr.io/nationalarchives/tna-python
ARG IMAGE_TAG=latest

FROM "$IMAGE":"$IMAGE_TAG"

# ...
```

...you can replace the `tna-python` image in your application with the dev version in your `docker-compose.yml`:

```diff
services:
  app:
-   build .
+   build:
+     context: .
+     args:
+       IMAGE: ghcr.io/nationalarchives/tna-python-dev
    environment:
      - ENVIRONMENT_NAME=develop
      - CONFIG=config.Develop
      - DEBUG=true
      - SECRET_KEY=abc123
      - NPM_DEVELOP_COMMAND=dev
    ports:
      - 65535:8080
    volumes:
      - ./:/app
```

The `Dockerfile` is used to generate the production image and so the default `tna-python:latest` image is used.

`docker-compose.yml` is only used for local development so we are safe to set custom image and versions here.

## Commands

Run `help` from within the container to see a list of available commands.

### `tna-wsgi` and `tna-asgi`

In the `tna-python-dev` image, both of these commands are replaced by a script that detects the frameworks used and runs their development servers.

This means you don't have to change anything in your `Dockerfile` when switching between `tna-python` and `tna-python-dev`.

The process for these commands is:

1. If `NPM_DEVELOP_COMMAND` has been defined then run `tna-node "$NPM_DEVELOP_COMMAND"` (See [tna-node](../tna-python/README.md#tna-node-command))
1. If Django is installed, run the Django development server
   1. Else if Flask is installed, run the Flask development server
   1. Else if FastAPI is installed, run the FastAPI development server

### `format`

1. Run `ruff` (using [tna-ruff-config](https://github.com/nationalarchives/ruff-config))
1. Run `djlint` to check HTML templates for Jinja compliance
1. Run `stylelint` against all SCSS files in the `/app` directory (using [@nationalarchives/stylelint-config](https://github.com/nationalarchives/stylelint-config))
1. Run `eslint` against all JavaScript files in the `/app` directory (using [@nationalarchives/eslint-config](https://github.com/nationalarchives/eslint-config))
1. Apply `prettier` to all files in the `/app` directory

#### Ruff

##### Extending the default Ruff configuration

Create a `ruff.toml` file in your project root. If this file exists, the `--strict` parameter will be ignored on `format --strict` and `checkformat --strict`.

```toml
# Extend the default Ruff configuration
extend = "/home/app/ruff.toml"

# ...or extend the strict ruleset
# extend = "/home/app/ruff-strict.toml"

extend-exclude = [
    # "migrations"  # Exclude the "migrations" directory
]

[lint]
ignore = [
    # Add rules to ignore in your project
]
```

##### Supressing errors

Use the `# noqa` annotation from [Ruff error suppression](https://docs.astral.sh/ruff/linter/#error-suppression) to ignore failing lines.

```python
def my_overly_complex_function():  # noqa: C901
    pass
```

#### How to override other default configurations

| Tool        | Overwrite solution                                                        | More information                                                                           |
| ----------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `djlint`    | `.djlintrc` file in the project root                                      | https://djlint.com/docs/configuration/                                                     |
| `stylelint` | `stylelint.config.mjs` and/or `.stylelintignore` file in the project root | https://stylelint.io/user-guide/configure/, https://stylelint.io/user-guide/ignore-code/   |
| `eslint`    | `eslint.config.mjs` file in the project root                              | https://eslint.org/docs/latest/use/configure/configuration-files#using-configuration-files |
| `prettier`  | `.prettierignore` file in the project root                                | https://prettier.io/docs/en/ignore.html                                                    |

### `checkformat`

Runs the same tests as `format` but doesn't fix issues. Can be used in CI/CD pipelines to check formatting.

Like `format --strict`, `checkformat --strict` uses an [expanded set of Ruff rules](#ruff).

### `outdated`

1. Shows outdated Poetry dependencies
1. Shows outdated npm dependencies

### `upgrade`

1. Updates Poetry dependencies
1. Updates npm dependencies

Run `upgrade poetry` to update only Poetry dependencies.

Run `upgrade npm` to update only npm dependencies.

### `secret-key`

Generate a string that can be used as the environment variable `SECRET_KEY`:

- https://docs.python.org/3/library/secrets.html
- https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
- https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY

## Custom development scripts

You can create a directory of custom scripts and mount it at `/home/app/.local/bin/tasks`.

This will allow you to run the scripts inside the dev Docker container. These could be used to migrate data, manipulate the database or run specific tests.

### Example

Create a file called `foo` in the `tasks` directory:

```bash
#!/bin/bash
echo "bar"
```

Mount the directory to `/home/app/.local/bin/tasks`:

```diff
services:
  app:
    build:
      context: .
      args:
        IMAGE: ghcr.io/nationalarchives/tna-python-dev
    environment:
      - ENVIRONMENT_NAME=develop
      - CONFIG=config.Develop
      - DEBUG=true
      - SECRET_KEY=abc123
      - NPM_DEVELOP_COMMAND=dev
    ports:
      - 65535:8080
    volumes:
      - ./:/app
+     - ./tasks:/home/app/.local/bin/tasks  # <-- Mount the tasks directory
```

Run your command from the host machine:

```sh
docker compose exec app foo
>>> bar
```

...or from within the container:

```sh
foo
>>> bar
```

## SSL

All SSL configuration is ignored in `tna-python-dev` and the plain development HTTP servers for each framework are used instead.
