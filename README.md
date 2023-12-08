<img src="https://raw.githubusercontent.com/nationalarchives/tna-frontend/main/src/nationalarchives/assets/images/tna-square-logo.svg" alt="The National Archives logo" title="The National Archives" width="100" />

# National Archives Base Docker Images

[![Main build status](https://img.shields.io/github/actions/workflow/status/nationalarchives/docker/publish.yml?style=flat-square&event=push&branch=main)](https://github.com/nationalarchives/docker/actions/workflows/publish.yml?query=branch%3Amain)
[![Latest release](https://img.shields.io/github/v/release/nationalarchives/docker?style=flat-square&logo=github&logoColor=white&sort=semver)](https://github.com/nationalarchives/docker/releases)
[![Licence](https://img.shields.io/github/license/nationalarchives/docker?style=flat-square)](https://github.com/nationalarchives/docker/blob/main/LICENCE)

The National Archives base Docker images are designed to serve as a starting point for all containerised applications in The National Archives.

## Base images

| Image                                           | Dockerfile                                                            | Base image        | User   |
| ----------------------------------------------- | --------------------------------------------------------------------- | ----------------- | ------ |
| [`tna-python`](docker/tna-python)               | [`tna-python/Dockerfile`](docker/tna-python/Dockerfile)               | `python`          | `app`  |
| `tna-python-root`                               | [`tna-python/Dockerfile`](docker/tna-python/Dockerfile)               | `python`          | `root` |
| [`tna-python-django`](docker/tna-python-django) | [`tna-python-django/Dockerfile`](docker/tna-python-django/Dockerfile) | `tna-python`      | `app`  |
| `tna-python-django-root`                        | [`tna-python-django/Dockerfile`](docker/tna-python-django/Dockerfile) | `tna-python-root` | `root` |
| [`tna-python-dev`](docker/tna-python-dev)       | [`tna-python-dev/Dockerfile`](docker/tna-python-dev/Dockerfile)       | `tna-python-root` | `root` |

### Image inheritance

```mermaid
graph TD;
    debian --> python;
    python --> tna-python;
    python --> tna-python-root;
    tna-python --> tna-python-django;
    tna-python-root --> tna-python-django-root;
    tna-python-root --> tna-python-dev;
```
