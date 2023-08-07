# tna-python

This image comes with:

- A version of Python approved by TNA
- [Poetry](https://python-poetry.org/) for dependency management
- [nvm](https://github.com/nvm-sh/nvm) for compiling assets such as CSS and JavaScript
- [Gunicorn](https://gunicorn.org/) for serving the Python application

This image requires you have the following files in the root of your project:

- `pyproject.toml`
- `poetry.lock`

## Environment variables

| Variable               | Description                                           | Default                                                        |
| ---------------------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| `ENVIRONMENT`          | The current environment[^1]                           | `production`                                                   |
| `WORKERS`              | Number of worker processes[^2]                        | `3` on `develop`, `(cpu * 2) + 1` elsewhere                    |
| `THREADS`              | Number of threads[^3]                                 | `3` on `develop`, `(cpu * 2) + 1` elsewhere                    |
| `LOG_LEVEL`            | The log level to stream to the console[^4]            | `WARN` on `production`, `DEBUG` on `develop`, `INFO` elsewhere |
| `NODE_ENV`             | The node environment which could affect the build[^5] | Copied from `ENVIRONMENT`                                      |
| `NPM_BUILD_COMMAND`    | The npm script to run to build static assets          | [None] - don't build anything by default                       |
| `NPM_DEVELOP_COMMAND`  | The npm script to run in development environments     | [None] - don't build and watch anything by default             |

[^1]: Predefined values are `production` and `develop` but any alphanumeric string is valid
[^2]: [Gunicorn docs - How Many Workers?](https://docs.gunicorn.org/en/latest/design.html#how-many-workers)
[^3]: [Gunicorn docs - How Many Threads?](https://docs.gunicorn.org/en/latest/design.html#how-many-threads)
[^4]: Supported levels are `CRITICAL`, `ERROR`, `WARN`, `INFO` and `DEBUG` (https://docs.gunicorn.org/en/latest/settings.html?highlight=log#loglevel)
[^5]: [Node.js, the difference between development and production](https://nodejs.dev/en/learn/nodejs-the-difference-between-development-and-production/)

## Commands for the Dockerfile

There are two commands to use within your `Dockerfile`:

- [`tna-build`](#tna-build)
- [`tna-run`](#tna-run)

### `tna-build`

1. Checks for the existance of a `pyproject.toml` and `poetry.lock` file
1. Checks for correct Node files (see ["Using Node"](#using-node)) and if they exist:
    1. Install the version of Node defined in `.nvmrc`
    1. Install all the Node dependencies (not `devDependencies`)
    1. Build the assets with the npm script defined in `$NPM_BUILD_COMMAND`
    1. Remove the whole `node_modules` directory
1. Add `gunicorn` to the project
1. Install all the dependencies found in `pyproject.toml`

### `tna-run`

`tna-run` takes one positional parameter which is the application module to be run, for example:

```sh
tna-run my_app:app
```

#### Process

1. If `$ENVIRONMENT` is set to `develop`, there is a `package.json` file and `$NPM_DEVELOP_COMMAND` has been defined:
    1. Use the version of Node defined in `.nvmrc` as was installed by `tna-build`
    1. Install all the Node dependencies
    1. Run the npm script `$NPM_DEVELOP_COMMAND`
1. Count the number of CPU cores, multiply it by 2 and add 1 to get a suggested worker and thread count
1. Start `gunicorn` with values appropriate to the environment taking into account any overrides

## Using Node

To use Node to build your assets you need three files in your project:

- `package.json`
- `package-lock.json`
- `.nvmrc`
