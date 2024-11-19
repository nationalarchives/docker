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

### `upgrade`

1. Updates Poetry dependencies
1. Updates npm dependencies

### `secret-key`

Generate a string that can be used as the environment variable `SECRET_KEY`:

- https://docs.python.org/3/library/secrets.html
- https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
- https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY

## Mountable scripts

You can create a directory of custom scripts and mount the directory to the volume `/home/app/.local/bin/tasks`.

This will allow you to run the scripts inside the dev Docker container. These could be used to migrate data, manipulate the database or run specific tests.

### Example

Create a file called `foo` in the `tasks` directory:

```sh
#!/bin/bash
echo "bar"
```

Mount the directory to `/home/app/.local/bin/tasks`:

```yml
services:
  dev:
    image: ghcr.io/nationalarchives/tna-python-dev:preview
    volumes:
      - ./:/app                             # Application code
      - ./tasks:/home/app/.local/bin/tasks  # Tasks directory
```

Run your command from the host machine:

```sh
docker compose exec dev foo
>>> bar
```

...or from within the container:

```sh
foo
>>> bar
```
