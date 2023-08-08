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

The two commands from `tna-python` (`tna-build` and `tna-run`) are moved to `tna-build-common` and `tna-run-common` and two new `tna-build` and `tna-run` commands are added.

### `tna-build`

1. Runs [`tna-build`](../tna-python/README.md#tna-build) from `tna-python` (now `tna-build-common`)
1. Collects static assets (requires setup and directories to be present)

### `tna-run`

As with `tna-run` command from `tna-python` (now `tna-run-common`), this takes one positional parameter which is the Django WSGI application module to be run, for example:

```sh
tna-run my_app.wsgi:application
```

For more information, see [how to deploy with WSGI](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/).

#### Process

1. Run any required Django migrations
1. Runs [`tna-run`](../tna-python/README.md#tna-run) from `tna-python` (now `tna-run-common`)
