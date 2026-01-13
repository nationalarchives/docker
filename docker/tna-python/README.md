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

Each environment has some default values but all can be overwritten:

| Variable                   | Description                                                               | Default                                   |
| -------------------------- | ------------------------------------------------------------------------- | ----------------------------------------- |
| `SECRET_KEY`               | A random key used to secure client session data                           | _none_                                    |
| `WORKERS`                  | Number of worker processes[^1]                                            | `(cpu * 2) + 1`                           |
| `THREADS`                  | Number of threads[^2]                                                     | `$WORKERS * 2` (ignored by `tna-asgi`)    |
| `LOG_LEVEL`                | The log level to stream to the console[^3][^4]                            | `tna-wsgi`: `warn`, `tna-asgi`: `warning` |
| `NODE_ENV`                 | The node environment[^5]                                                  | `production`                              |
| `NPM_BUILD_COMMAND`        | The npm script from `package.json` to run to build static assets          | _none_                                    |
| `TIMEOUT`                  | The number of seconds before a request is terminated[^6]                  | `30` (ignored by `tna-asgi`)              |
| `KEEP_ALIVE`               | The number of seconds to wait for requests on a keep-alive connection[^7] | `30`                                      |
| `ALLOW_INSECURE`           | If `true`, use HTTP rather than HTTPS                                     | `false`                                   |
| `SSL_KEY_FILE`             | The location of the SSL key                                               | `/home/app/ssl/server.key`                |
| `SSL_CERTIFICATE_FILE`     | The location of the SSL certificate                                       | `/home/app/ssl/server.crt`                |
| `SSL_CA_CERTIFICATES_FILE` | The location of the CA certificates                                       | _none_                                    |
| `SSL_DOMAIN`               | Domain for a self-signed SSL if no key or certificate files are provided  | _none_                                    |
| `PORT`                     | Set the port used by the container (only used outside of AWS)             | `8080`                                    |

[^1]: [Gunicorn docs - How Many Workers?](https://docs.gunicorn.org/en/latest/design.html#how-many-workers)

[^2]: [Gunicorn docs - How Many Threads?](https://docs.gunicorn.org/en/latest/design.html#how-many-threads)

[^3]: Supported levels for Gunicorn are `critical`, `error`, `warn`, `info` and `debug` [Gunicorn docs - log level](https://docs.gunicorn.org/en/latest/settings.html?highlight=log#loglevel)

[^4]: Supported levels for Uvicorn are `critical`, `error`, `warning`, `info`, `debug` and `trace` [Uvicorn docs - logging settings](https://uvicorn.dev/settings/#logging)

[^5]: [Node.js, the difference between development and production](https://nodejs.dev/en/learn/nodejs-the-difference-between-development-and-production/)

[^6]: [Gunicorn docs - timeout](https://docs.gunicorn.org/en/stable/settings.html#timeout)

[^7]: [Gunicorn docs - keepalive](https://docs.gunicorn.org/en/stable/settings.html#keepalive)

## Commands for the Dockerfile

Commands available to use within your `Dockerfile`:

- [`tna-build`](#tna-build)
- [`tna-node`](#tna-node-command)
- [`tna-npm`](#tna-npm-command)
- [`tna-clean`](#tna-clean)
- [`tna-wsgi` and `tna-asgi`](#tna-wsgi-and-tna-asgi)

### `tna-build`

1. Checks for the presence of `pyproject.toml` and `poetry.lock` files
1. If `$NPM_BUILD_COMMAND` is defined, run `tna-node "$NPM_BUILD_COMMAND"` (See [tna-node](#tna-node-command))
1. Installs `gunicorn`, `uvicorn`, `uvicorn-worker`
1. Installs `tool.poetry.dependencies` from `pyproject.toml`
   - `tna-python-dev` image also installs `tool.poetry.group.dev.dependencies`
1. In `tna-python-django`, collect all static assets if `django.contrib.staticfiles` is used

### `tna-node [command]`

1. Checks for the presence of a `package.json` file
1. Installs Node dependencies from `package.json` using [tna-npm](#tna-npm-command)
1. Runs the passed `[command]` as `npm run [command]` (e.g. `build` from in `package.json`) using [tna-npm](#tna-npm-command)

### `tna-npm [command]`

1. Sets the Node version to that defined in `.nvmrc`
   - If `.nvmrc` is not defined, use the `default` nvm version
1. Runs the passed `[command]` as `npm [command]` (e.g. `install @nationalarchives/frontend`)

### `tna-clean`

1. Removes `node_modules` directory
1. Removes npm and nvm
1. Removes `tna-build`, `tna-node` and `tna-nvm` scripts

### `tna-wsgi` and `tna-asgi`

Both `tna-wsgi` and `tna-asgi` take one positional parameter which is the application module to be run, for example:

```sh
tna-wsgi my_app:app
tna-asgi my_app:app
```

The process for these commands is:

1. If `$NPM_BUILD_COMMAND` has been defined then run it to build any resources using [`tna-node [command]`](#tna-node-command)
1. Calculate the default worker and thread count based on the number of CPU cores
1. Start `gunicorn` (`tna-wsgi`) or `uvicorn` (`tna-asgi`) with values appropriate to the environment taking into account any overrides

## Using Node

To use Node to build your assets you need three files in your project:

- `package.json`
- `package-lock.json`
- `.nvmrc` containing the version of Node you would like to support (e.g. `lts/iron`)

## SSL

The WSGI or ASGI can run behind SSL if you provide the certificates.

Two files need to be mounted to the container in order to use SSL:

- `/home/app/ssl/key.pem`
- `/home/app/ssl/cert.pem`

Ensure the files can be read by the container user.

These locations can be overridden with the `SSL_KEY_FILE` and `SSL_CERTIFICATE_FILE` environment variables.

Set the `SSL_CA_CERTIFICATES_FILE` environment variable and mount an appropriate CA file to the container to set up the certificate authorities.

SSL for the containers can be disabled by setting `ALLOW_INSECURE` to `true`.
