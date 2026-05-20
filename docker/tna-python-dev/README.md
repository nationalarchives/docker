# tna-python-dev

> ⚠️ Do not use `tna-python-dev` in production

This image extends `tna-python` and can be used for local development **ONLY**. It adds:

- `ruff` for formatting and linting Python
- `prettier`, `eslint` and `stylelint` for formatting JavaScript and CSS
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

1. Run `ruff`
1. Run `djlint` to check HTML templates for Jinja compliance
1. Apply `prettier` to all files in the `/app` directory
1. Run `stylelint` against all SCSS files in the `/app` directory
1. Run `eslint` against all JavaScript files in the `/app` directory

#### Ruff

By default, Ruff is only configured to check the following when running `format` and `checkformat`:

| Code             | Purpose                                                                         | Defined by                                                               |
| ---------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `E4`, `E7`, `E9` | [Subset of pycodestyle errors](https://pypi.org/project/pycodestyle/)           | [Ruff default configuration](https://docs.astral.sh/ruff/configuration/) |
| `F`              | [Pyflakes](https://pypi.org/project/pyflakes/)                                  | [Ruff default configuration](https://docs.astral.sh/ruff/configuration/) |
| `W`              | [pycodestyle warnings](https://pypi.org/project/pycodestyle/)                   | [`/home/app/ruff.toml`](./lib/ruff.toml)                                 |
| `C901`           | [mccabe "Function is too complex"](https://www.flake8rules.com/rules/C901.html) | [`/home/app/ruff.toml`](./lib/ruff.toml)                                 |
| `B`              | [flake8-bugbear](https://pypi.org/project/flake8-bugbear/)                      | [`/home/app/ruff.toml`](./lib/ruff.toml)                                 |
| `I`              | [isort](https://pypi.org/project/isort/)                                        | [`/home/app/ruff.toml`](./lib/ruff.toml)                                 |
| `Q`              | [flake8-quotes](https://pypi.org/project/flake8-quotes/)                        | [`/home/app/ruff.toml`](./lib/ruff.toml)                                 |

Running `format --strict` or `checkformat --strict` will apply some extra rules defined in [`/home/app/ruff-strict.toml`](./lib/ruff-strict.toml):

| Code   | Purpose                                                               |
| ------ | --------------------------------------------------------------------- |
| `A`    | [flake8-builtins](https://pypi.org/project/flake8-builtins/)          |
| `DJ`   | [flake8-django](https://pypi.org/project/flake8-django/)              |
| `ERA`  | [eradicate](https://pypi.org/project/eradicate/)                      |
| `FAST` | [fastapi](https://pypi.org/project/fastapi/)                          |
| `FIX`  | [flake8-fixme](https://github.com/tommilligan/flake8-fixme)           |
| `LOG`  | [flake8-logging](https://pypi.org/project/flake8-logging/)            |
| `N`    | [pep8-naming](https://pypi.org/project/pep8-naming/)                  |
| `PL`   | [pylint](https://pypi.org/project/pylint/)                            |
| `RET`  | [flake8-return](https://pypi.org/project/flake8-return/)              |
| `RSE`  | [flake8-raise](https://pypi.org/project/flake8-raise/)                |
| `RUF`  | [Ruff-specific rules](https://docs.astral.sh/ruff/settings/#lintruff) |
| `SIM`  | [flake8-simplify](https://pypi.org/project/flake8-simplify/)          |
| `T20`  | [flake8-print](https://pypi.org/project/flake8-print/)                |
| `TD`   | [flake8-todos](https://github.com/orsinium-labs/flake8-todos/)        |
| `TRY`  | [tryceratops](https://pypi.org/project/tryceratops/)                  |
| `UP`   | [pyupgrade](https://pypi.org/project/pyupgrade/)                      |

##### How to override Ruff configuration

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

##### Ignoring code

Use the `# noqa` annotation from [In-line Ignoring Errorsin Flake8](https://flake8.pycqa.org/en/latest/user/violations.html#in-line-ignoring-errors) to ignore failing lines.

```python
def my_overly_complex_function():  # noqa: C901
    pass
```

#### How to override other default configurations

| Tool        | Overwrite solution                           | More information                                                                           |
| ----------- | -------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `djlint`    | `.djlintrc` file in the project root         | https://djlint.com/docs/configuration/                                                     |
| `prettier`  | `.prettierignore` file in the project root   | https://prettier.io/docs/en/ignore.html                                                    |
| `stylelint` | `.stylelintrc` file in the project root      | https://stylelint.io/user-guide/configure/                                                 |
| `eslint`    | `eslint.config.mjs` file in the project root | https://eslint.org/docs/latest/use/configure/configuration-files#using-configuration-files |

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
