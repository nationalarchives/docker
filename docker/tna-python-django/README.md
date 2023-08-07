# tna-python-django

This image extends `tna-python` but adds:

- ???

This image assumes you have a version of Django added to you project's `pyproject.toml` file.

## Environment variables

All environment variables defined in [tna-python](../tna-python/README.md) as well as:

| Variable                  | Description                                 | Default                     |
| ------------------------- | ------------------------------------------- | --------------------------- |
| `DJANGO_SETTINGS_MODULE`  | Which Django settings module to load        | [None]                      |

## Commands for the Dockerfile

In addition to the two commands from `tna-python` (`tna-build` && `tna-run`) there is a `tna-build-django` command.

The `tna-run` command is replaced with a Django-specific command but the `tna-build-django` extends the existing `tna-build`.

### `tna-build-django`

1. Runs [`tna-build`](../tna-python/README.md#tna-build)
1. Collects static assets (if defined)

### `tna-run-django`

As with `tna-run` command from `tna-python`, `tna-run-django` takes one positional parameter which is the Django WSGI application module to be run, for example:

```sh
tna-run-django my_app.wsgi:application
```

For more information, see [how to deploy with WSGI](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/).

#### Process

1. If `$ENVIRONMENT` is set to `develop`, there is a `package.json` file and `$NPM_DEVELOP_COMMAND` has been defined:
    1. Use the version of Node defined in `.nvmrc` as was installed by `tna-build`
    1. Install all the Node dependencies
    1. Run the npm script `$NPM_DEVELOP_COMMAND`
1. Count the number of CPU cores, multiply it by 2 and add 1 to get a suggested worker and thread count
1. Start `gunicorn` with values appropriate to the environment taking into account any overrides

