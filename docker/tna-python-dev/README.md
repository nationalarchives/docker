# tna-python-dev

> ⚠️ Do not use `tna-python-dev` in production

This image extends `tna-python` and can be used for local development **ONLY**. It adds:

- `black`, `flake8` and `isort` for formatting Python code
- `prettier`, `eslint` and `stylelint` for formatting JavaScript and CSS
- scripts for formatting code
- `django-debug-toolbar` for debugging Django applications
- `git`

## Environment variables

All environment variables extended from [tna-python](../tna-python/README.md) but with different defaults:

| Variable               | Default       |
| ---------------------- | ------------- |
| `WORKERS`              | `3`           |
| `THREADS`              | `3`           |
| `LOG_LEVEL`            | `debug`       |
| `NODE_ENV`             | `development` |
| `TIMEOUT`              | `600`         |
| `KEEP_ALIVE`           | `5`           |
| `SSL_KEY_FILE`         | _ignored_     |
| `SSL_CERTIFICATE_FILE` | _ignored_     |
| `ALLOW_INSECURE`       | _ignored_     |

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

1. Run `isort`
1. Run `black`
1. Run `flake8`
1. Apply `prettier` to all files in the `/app` directory
1. Run `stylelint` against all SCSS files in the `/app` directory
1. Run `eslint` against all JavaScript files in the `/app` directory

#### How to override the default configurations

| Tool        | Overwrite solution                                | More information                                                                                        |
| ----------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `isort`     | `.isort.cfg` file in the project root             | https://pycqa.github.io/isort/docs/configuration/config_files.html#isortcfg-preferred-format            |
| `black`     | Add `[tool.black]` config to the `pyproject.toml` | https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file |
| `flake8`    | `.flake8` file in the project root                | https://flake8.pycqa.org/en/latest/user/configuration.html#configuration-locations                      |
| `prettier`  | `.prettierignore` file in the project root        | https://prettier.io/docs/en/ignore.html                                                                 |
| `stylelint` | `.stylelintrc` file in the project root           | https://stylelint.io/user-guide/configure/                                                              |
| `eslint`    | `.eslintrc.js` file in the project root           | https://eslint.org/docs/latest/use/configure/configuration-files#using-configuration-files              |

### `checkformat`

Runs the same tests as `format` but doesn't fix issues. Can be used in CI/CD pipelines to check formatting.

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
