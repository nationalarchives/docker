# tna-python

This image comes with:

- A version of Python approved by TNA
- [Poetry](https://python-poetry.org/) for dependency management
- [nvm](https://github.com/nvm-sh/nvm) for compiling assets such as CSS and JavaScript
- [Gunicorn](https://gunicorn.org/) for serving the Python application via WSGI or ASGI, added to the project when `tna-build` runs

This image requires you have the following files in the root of your project:

- `pyproject.toml`
- `poetry.lock`

## Environment variables

Each environment has some default values but all can be overwritten:

| Variable                   | Description                                                                 | Default                        |
| -------------------------- | --------------------------------------------------------------------------- | ------------------------------ |
| `SECRET_KEY`               | A random key used to secure client session data                             | _none_                         |
| `WORKERS`                  | Number of worker processes[^1]                                              | `(cpu * 2) + 1`                |
| `THREADS`                  | Number of threads for threaded worker classes[^2]                           | `1` (ignored if using ASGI)    |
| `WORKER_CLASS`             | Gunicorn worker class                                                       | `sync` (`asgi` for `tna-asgi`) |
| `GUNICORN_PROTOCOL`        | Request protocol handled by Gunicorn                                        | `http` (`http` or `uwsgi`)     |
| `WORKER_CONNECTIONS`       | Maximum simultaneous clients for worker classes that support this setting   | `1000`                         |
| `MAX_REQUESTS`             | Maximum requests a worker handles before restarting                         | `0`                            |
| `MAX_REQUESTS_JITTER`      | Random variation added to the maximum requests                              | `0`                            |
| `LOG_LEVEL`                | The log level to stream to the console[^3]                                  | `warning`                      |
| `NODE_ENV`                 | The node environment[^4]                                                    | `production`                   |
| `NPM_BUILD_COMMAND`        | The npm script from `package.json` to run during `tna-build`                | _none_                         |
| `TIMEOUT`                  | Seconds a worker can remain silent before it is restarted[^5]               | `30`                           |
| `GRACEFUL_TIMEOUT`         | Seconds workers have to finish requests after a restart signal              | `30`                           |
| `KEEP_ALIVE`               | The number of seconds to wait for requests on a keep-alive connection[^6]   | `65`                           |
| `HTTP_PROTOCOLS`           | HTTP versions enabled by Gunicorn (for example, `h1` or `h2,h1`)            | `h1`                           |
| `ROOT_PATH`                | Root path for ASGI applications mounted below a URL prefix                  | _none_                         |
| `PRELOAD_APP`              | Load the application before forking worker processes                        | `false`                        |
| `APPLICATION_PORT`         | Port on which the application listens                                       | `8080`                         |
| `APPLICATION_PROTOCOL`     | The protocol of the application (`http` or `https`)                         | `https`                        |
| `SSL_KEY_FILE`             | The location of the SSL key                                                 | `/home/app/ssl/server.key`     |
| `SSL_CERTIFICATE_FILE`     | The location of the SSL certificate                                         | `/home/app/ssl/server.crt`     |
| `SSL_CA_CERTIFICATES_FILE` | The location of the CA certificates                                         | _none_                         |
| `SSL_DOMAIN`               | Domain used to generate a self-signed certificate if an SSL file is missing | _none_                         |

[^1]: [Gunicorn docs - How Many Workers?](https://docs.gunicorn.org/en/latest/design.html#how-many-workers)

[^2]: [Gunicorn docs - How Many Threads?](https://docs.gunicorn.org/en/latest/design.html#how-many-threads)

[^3]: Supported levels for Gunicorn are `critical`, `error`, `warning`, `info` and `debug` [Gunicorn docs - log level](https://gunicorn.org/reference/settings/#loglevel)

[^4]: [Node.js, the difference between development and production](https://nodejs.dev/en/learn/nodejs-the-difference-between-development-and-production/)

[^5]: [Gunicorn docs - timeout](https://docs.gunicorn.org/en/stable/settings.html#timeout)

[^6]: [Gunicorn docs - keepalive](https://docs.gunicorn.org/en/stable/settings.html#keepalive)

## Commands for the Dockerfile

Commands available to use within your `Dockerfile`:

- [`tna-build`](#tna-build)
- [`tna-node`](#tna-node-command)
- [`tna-clean`](#tna-clean)
- [`tna-wsgi` and `tna-asgi`](#tna-wsgi-and-tna-asgi)

### `tna-build`

1. Checks for the presence of `pyproject.toml` and `poetry.lock` files
1. Adds the pinned Gunicorn version to the project with Poetry
1. Installs `tool.poetry.dependencies` from `pyproject.toml`
   - `tna-python-dev` image also installs `tool.poetry.group.dev.dependencies`
1. If `$NPM_BUILD_COMMAND` is defined, run `tna-node "$NPM_BUILD_COMMAND"` (see [tna-node](#tna-node-command))

### `tna-node [command]`

1. Requires `package.json` and `package-lock.json` in `/app`
1. Uses the Node version in `.nvmrc`, or the image's default Node version if `.nvmrc` is absent
1. Runs `npm install --production=false`
1. Runs the passed script as `npm run [command]` (for example, `tna-node build` runs the `build` script in `package.json`)

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

1. Validate and load the Gunicorn configuration.
1. Start Gunicorn with the configured settings and environment-variable overrides.

`tna-asgi` sets `WORKER_CLASS=asgi`; `tna-wsgi` uses `WORKER_CLASS` or defaults to `sync`. `NPM_BUILD_COMMAND` is run by `tna-build`, not by these startup commands.

The default Gunicorn settings are loaded from `/home/app/gunicorn.conf.py`. To provide your own Gunicorn configuration, add `gunicorn.conf.py` to the application root (`/app`); it takes precedence over the default configuration.
The default configuration uses automatic ASGI event-loop and lifespan detection (`asgi_loop` and `asgi_lifespan` are both `auto`).

## Using Node

To use Node to build assets, provide these files in your project:

- `package.json`
- `package-lock.json`
- Optionally, `.nvmrc` containing the version of Node to use (for example, `lts/iron`). If omitted, the image's default Node version is used.

## SSL

### Self-signed certificates

If either the configured SSL key or certificate file is missing at startup, set `SSL_DOMAIN` to allow a self-signed certificate to be generated. The generated files are written to the default paths (`/home/app/ssl/server.key` and `/home/app/ssl/server.crt`).

The generated certificate will be valid for 10 years.

### Custom certificates

Mount two files in the container to use SSL:

- `/home/app/ssl/server.key`
- `/home/app/ssl/server.crt`

Ensure the files can be read by the container user.

These locations can be overridden with the `SSL_KEY_FILE` and `SSL_CERTIFICATE_FILE` environment variables.

#### Client certificate authorities

To verify client certificates, mount the CA file in the container (for example, at `/home/app/ssl/ca.crt`) and set `SSL_CA_CERTIFICATES_FILE` to its path. Gunicorn uses this file for TLS client-certificate verification.

### Disabling SSL

SSL for the containers can be disabled by setting `APPLICATION_PROTOCOL` to `http`.
