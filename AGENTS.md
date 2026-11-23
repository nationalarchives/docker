# Agent instructions

## Repository overview

This repository builds and publishes two Docker images:

- `docker/tna-python` is the production base image.
- `docker/tna-python-dev` extends the production image for development.

Each image's `Dockerfile`, `README.md`, and `bin/` scripts are maintained together. The root `README.md` documents the images and local build commands.

## Production and development images

The production image is intended for running the application in a secure, non-root environment with all necessary dependencies installed.

The development image extends the production image with additional tools and configurations to facilitate development and debugging and can be used as a drop-in replacement for the production image during development.

## Making changes

- Keep changes focused on the image or scripts involved, and update the related README when behavior or configuration changes.
- Preserve existing image conventions, including pinned package versions, non-root execution for the production image, and `/app` as the application working directory.
- Keep CI checks in `.github/workflows/` and `.github/actions/` aligned with changes to image behavior.
- Dockerfiles and scripts should be checked with ShellCheck for potential issues and best practices.
- Dockerfiles are also checked with Hadolint for best practices and potential issues.

## Validation

Build the production image after changes to it:

```sh
docker build --tag tna-python:local docker/tna-python
```

For development-image changes, build the production image first, then build the development image:

```sh
docker build --tag tna-python-dev:local \
  --build-arg BASE_IMAGE=tna-python \
  --build-arg BASE_IMAGE_TAG=local \
  docker/tna-python-dev
```

The CI workflow also lints Dockerfiles, runs ShellCheck on image scripts, builds both images, and tests them with Flask, Django, and FastAPI application templates.
