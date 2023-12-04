# tna-python-flask

This image extends `tna-python` but adds checks for environment variables specific to Flask.

This image assumes you have a version of Flask added to you project's `pyproject.toml` file.

## Environment variables

All environment variables defined in [tna-python](../tna-python/README.md) as well as:

| Variable     | Description                                     | Default |
| ------------ | ----------------------------------------------- | ------- |
| `SECRET_KEY` | A random key used to secure client session data | [None]  |

A secret key can be generated using:

```sh
python -c 'import secrets; print(secrets.token_hex())'
```

## Commands for the Dockerfile

The command `tna-run` is moved to `tna-run-common` and a new and `tna-run` command is added.
