# tna-python

This image comes with:

- A version of Python approved by TNA
- [Poetry](https://python-poetry.org/) for dependency management
- [nvm](https://github.com/nvm-sh/nvm) for compiling assets such as CSS and JavaScript
- [Gunicorn](https://gunicorn.org/) for serving the Python application

## Environment variables

| Variable              | Description                                       | Default                                                        |
| --------------------- | ------------------------------------------------- | -------------------------------------------------------------- |
| `ENVIRONMENT`         | The current environment[^1]                       | `production`                                                   |
| `WORKERS`             | Number of worker processes[^2]                    | `3` on `develop`, `(cpu * 2) + 1` elsewhere                    |
| `THREADS`             | Number of threads[^3]                             | `3` on `develop`, `(cpu * 2) + 1` elsewhere                    |
| `LOG_LEVEL`           | The log level to stream to the console[^4]        | `WARN` on `production`, `DEBUG` on `develop`, `INFO` elsewhere |
| `NODE_ENV`            | The node environment which could affect the build | Copied from `ENVIRONMENT`                                      |
| `NPM_BUILD_COMMAND`   | The npm script to run to build static assets      | `build`                                                        |
| `NPM_DEVELOP_COMMAND` | The npm script to run in development environments | `dev`                                                          |

### Sources

[^1]: Predefined values are `production` and `develop` but any alphanumeric string is valid
[^2]: [Gunicorn docs - How Many Workers?](https://docs.gunicorn.org/en/latest/design.html#how-many-workers)
[^3]: [Gunicorn docs - How Many Threads?](https://docs.gunicorn.org/en/latest/design.html#how-many-threads)
[^4]: Supported levels are `CRITICAL`, `ERROR`, `WARN`, `INFO` and `DEBUG` (https://docs.gunicorn.org/en/latest/settings.html?highlight=log#loglevel)

## Using Node

To use Node to build your assets you need three files in your project:

- `package.json`
- `package-lock.json`
- `.nvmrc`
