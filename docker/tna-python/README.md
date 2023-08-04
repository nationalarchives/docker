# tna-python

## Environment variables

| Variable      | Description                                | Default                                                        |
| ------------- | ------------------------------------------ | -------------------------------------------------------------- |
| `ENVIRONMENT` | The current environment[^1]                | `production`                                                   |
| `WORKERS`     | Number of worker processes[^2]             | `1` on `develop`, `(cpu * 2) + 1` elsewhere                    |
| `THREADS`     | Number of threads[^3]                      | `1` on `develop`, `(cpu * 2) + 1` elsewhere                    |
| `LOG_LEVEL`   | The log level to stream to the console[^4] | `WARN` on `production`, `DEBUG` on `develop`, `INFO` elsewhere |

### Sources

[^1]: Predefined values are `production` and `develop` but any alphanumeric string is valid
[^2]: [Gunicorn docs - How Many Workers?](https://docs.gunicorn.org/en/latest/design.html#how-many-workers)
[^3]: [Gunicorn docs - How Many Threads?](https://docs.gunicorn.org/en/latest/design.html#how-many-threads)
[^4]: Supported levels are `CRITICAL`, `ERROR`, `WARN`, `INFO` and `DEBUG` (https://docs.gunicorn.org/en/latest/settings.html?highlight=log#loglevel)
