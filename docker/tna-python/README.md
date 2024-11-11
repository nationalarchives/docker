# tna-python

This image comes with:

- A version of Python approved by TNA
- [Poetry](https://python-poetry.org/) for dependency management
- [nvm](https://github.com/nvm-sh/nvm) for compiling assets such as CSS and JavaScript
- [Gunicorn](https://gunicorn.org/) for serving the Python application via a WSGI
- [Uvicorn](https://www.uvicorn.org/) for serving the Python application via a ASGI

This image requires you have the following files in the root of your project:

- `pyproject.toml`
- `poetry.lock`

## Environment variables

The three default environment names are:

- `production`
- `staging`
- `develop`

Any other alphanumeric string is considered a valid environment name but won't have predefined settings.

| Variable               | Description                                                               | Production default       | Staging default          | Develop default          | Other envs default       |
| ---------------------- | ------------------------------------------------------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `SECRET_KEY`           | A random key used to secure client session data                           | _none_                   | _none_                   | _none_                   | _none_                   |
| `WORKERS`              | Number of worker processes[^1]                                            | `(cpu * 2) + 1`          | `(cpu * 2) + 1`          | `3`                      | `(cpu * 2) + 1`          |
| `THREADS`              | Number of threads[^2]                                                     | `(cpu * 2) + 1`          | `(cpu * 2) + 1`          | `3`                      | `(cpu * 2) + 1`          |
| `LOG_LEVEL`            | The log level to stream to the console[^3]                                | `warn`                   | `debug`                  | `debug`                  | `info`                   |
| `NODE_ENV`             | The node environment[^4]                                                  | Mirrors `ENVIRONMENT`    | Mirrors `ENVIRONMENT`    | Mirrors `ENVIRONMENT`    | Mirrors `ENVIRONMENT`    |
| `NPM_BUILD_COMMAND`    | The npm script to run to build static assets                              | _none_                   | _none_                   | _none_                   | _none_                   |
| `NPM_DEVELOP_COMMAND`  | The npm script to run in development environments                         | _ignored_                | _ignored_                | _none_                   | _ignored_                |
| `TIMEOUT`              | The number of seconds before a request is terminated[^5]                  | `30`                     | `30`                     | `600`                    | `30`                     |
| `KEEP_ALIVE`           | The number of seconds to wait for requests on a keep-alive connection[^6] | `30`                     | `30`                     | `5`                      | `5`                      |
| `SSL_KEY_FILE`         | The location of the SSL key                                               | `/home/app/ssl/key.pem`  | `/home/app/ssl/key.pem`  | `/home/app/ssl/key.pem`  | `/home/app/ssl/key.pem`  |
| `SSL_CERTIFICATE_FILE` | The location of the SSL certificate                                       | `/home/app/ssl/cert.pem` | `/home/app/ssl/cert.pem` | `/home/app/ssl/cert.pem` | `/home/app/ssl/cert.pem` |

[^1]: [Gunicorn docs - How Many Workers?](https://docs.gunicorn.org/en/latest/design.html#how-many-workers)

[^2]: [Gunicorn docs - How Many Threads?](https://docs.gunicorn.org/en/latest/design.html#how-many-threads)

[^3]: Supported levels are `critical`, `error`, `warn`, `info` and `debug` [Gunicorn docs - log level](https://docs.gunicorn.org/en/latest/settings.html?highlight=log#loglevel)

[^4]: [Node.js, the difference between development and production](https://nodejs.dev/en/learn/nodejs-the-difference-between-development-and-production/)

[^5]: [Gunicorn docs - timeout](https://docs.gunicorn.org/en/stable/settings.html#timeout)

[^6]: [Gunicorn docs - keepalive](https://docs.gunicorn.org/en/stable/settings.html#keepalive)

### Secret key

A secret key (for `SECRET_KEY`) can be generated using:

```sh
python -c 'import secrets; print(secrets.token_hex())'
```

Alternatively, using the [`tna-dev` image](https://github.com/nationalarchives/docker/tree/main/docker/tna-python-dev), you can run `secret-key` to generate one.

## Commands for the Dockerfile

There are two commands to use within your `Dockerfile`:

- [`tna-build`](#tna-build)
- [`tna-node`](#tna-node-command)
- [`tna-run`](#tna-run)

### `tna-build`

1. Checks for the presence of `pyproject.toml` and `poetry.lock` files
1. If `$NPM_BUILD_COMMAND` is defined, run `tna-node "$NPM_BUILD_COMMAND"` (See [tna-node](#tna-node-command))
1. Installs `gunicorn`, `uvicorn`, `uvicorn-worker`
1. Installs `tool.poetry.dependencies` from `pyproject.toml`
   - `tna-python-dev` image also installs `tool.poetry.group.dev.dependencies`
1. In `tna-python-django`, collect all static assets if `django.contrib.staticfiles` is used

### `tna-node [command]`

1. Checks for the presence of `package.json`, `package-lock.json` and `.nvmrc` files
1. Sets the Node version to that defined in `.nvmrc`
1. Installs Node dependencies from `package.json`
1. Runs the passed `[command]` as `npm run [command]` (e.g. `build` from in `package.json`)

### `tna-run`

`tna-run` takes one positional parameter which is the application module to be run, for example:

```sh
tna-run my_app:app
```

#### Process

1. In `tna-python-django`, run all database migrations
1. If `$ENVIRONMENT` is set to `develop` and `$NPM_DEVELOP_COMMAND` has been defined then run `tna-node "$NPM_DEVELOP_COMMAND"` (See [tna-node](#tna-node))
1. Calculate the default worker and thread count based on the number of CPU cores
1. If `$ENVIRONMENT` is set to `develop`:
   1. If Django is installed, run the Django development server
   1. Else if Flask is installed, run the Flask development server
   1. Else if FastAPI is installed, run uvicorn with reloading
   1. Else run the application through gunicorn with reloading using the async worker if the `-a` flag is passed
1. Else for any other environment, start `gunicorn` with values appropriate to the environment taking into account any overrides

#### Asynchronous support

For frameworks that require or can use an ASGI rather than a WSGI you can use `tna-run` with a `-a` flag:

```sh
tna-run -a my_app:app
```

When working in a development environment (`ENVIRONMENT=production`) and using FastAPI, Uvicorn is used as the ASGI for `tna-run`.

When using FastAPI in production, `tna-run -a` should be explicitly specified so Gunicron can use the Uvicorn worker class.

## Using Node

To use Node to build your assets you need three files in your project:

- `package.json`
- `package-lock.json`
- `.nvmrc` containing the version of Node you would like to support (e.g. `lts/iron`)

## Using SSL

On all environments apart from `develop`, an SSL certificate is required.

Two files need to be mounted to the container in order to run environments outside of development:

- `/home/app/ssl/key.pem`
- `/home/app/ssl/cert.pem`

These locations can be overridden with the `SSL_KEY_FILE` and `SSL_CERTIFICATE_FILE` environment variables.
