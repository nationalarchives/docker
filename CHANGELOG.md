# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/nationalarchives/docker/compare/v0.2.8...HEAD)

### Added
### Changed

- Make `SECRET_KEY` optional

### Deprecated
### Removed
### Fixed
### Security

## [0.2.8](https://github.com/nationalarchives/docker/compare/v0.2.7...v0.2.8) - 2024-07-16

### Added

- Add a `staging` environment

### Changed

- Updated Poetry to [1.8.3](https://github.com/python-poetry/poetry/releases/tag/1.8.3)
- Updated Gunicorn to [22.0.0](https://github.com/benoitc/gunicorn/releases/tag/22.0.0)
- Updated Uvicorn to [0.30.1](https://github.com/encode/uvicorn/releases/tag/0.30.1) and switched to [uvicorn-worker](https://github.com/Kludex/uvicorn-worker)
- Make `SECRET_KEY` optional
- Allow more configuration file types for stylelint and eslint

### Fixed

- Flask apps with factories are now explicitly run using the provided entrypoint

## [0.2.7](https://github.com/nationalarchives/docker/compare/v0.2.6...v0.2.7) - 2024-04-08

### Fixed

- Manifests fixed

## [0.2.6](https://github.com/nationalarchives/docker/compare/v0.2.5...v0.2.6) - 2024-04-05

### Removed

- Removed fix for [CVE-2022-40897](https://access.redhat.com/security/cve/cve-2022-40897)

## [0.2.5](https://github.com/nationalarchives/docker/compare/v0.2.4...v0.2.5) - 2024-03-27

### Changed

- Updated Poetry to [1.8.2](https://github.com/python-poetry/poetry/releases/tag/1.8.2)

## [0.2.4](https://github.com/nationalarchives/docker/compare/v0.2.3...v0.2.4) - 2024-02-27

### Changed

- Updated Poetry to [1.8.1](https://github.com/python-poetry/poetry/releases/tag/1.8.1)

## [0.2.3](https://github.com/nationalarchives/docker/compare/v0.2.2...v0.2.3) - 2024-02-19

### Changed

- Updated `prettier`, `eslint`, `stylelint`, `stylelint-config-standard-scss` and `stylelint-selector-bem-pattern` in `tna-python-dev`
- Updated `black`, `flake8` and `isort` in `tna-python-dev`
- Updated `nvm`

### Security

- Updated `libcurl4` and `curl`

## [0.2.2](https://github.com/nationalarchives/docker/compare/v0.2.1...v0.2.2) - 2024-01-23

### Changed

- Ignore `venv*,__pycache__,node_modules,migrations` in Flake8 configuration

## [0.2.1](https://github.com/nationalarchives/docker/compare/v0.2.0...v0.2.1) - 2024-01-15

### Changed

- Added trailing slash to healthcheck liveliness URI (`/healthcheck/live/`)

## [0.2.0](https://github.com/nationalarchives/docker/compare/v0.1.11...v0.2.0) - 2024-01-02

### Added

- Initial release of `tna-python-dev` Docker image
- Added `uvicorn` support for async applications such as FastAPI

### Changed

- Update Poetry to [1.7.1](https://github.com/python-poetry/poetry/releases/tag/1.7.1)
- Updated Base Docker image from `python:3.11-slim` to `python:3.12-slim-bookworm`
- Install `libcurl4` version `7.88.1-10+deb12u4`

### Security

- Upgrade all Debian packages

## [0.1.11](https://github.com/nationalarchives/docker/compare/v0.1.10...v0.1.11) - 2023-10-16

### Added

- New `-root` images which mirror their parents with the exception that they are run under the `root` user for development purposes

### Security

- Update `curl` to `7.88.1-10+deb12u4`

## [0.1.10](https://github.com/nationalarchives/docker/compare/v0.1.9...v0.1.10) - 2023-08-29

### Added

- Installed `libmagic-dev` to enable `libmagic`
- Installed Node `lts/hydrogen` using `nvm` to aid faster build times for projects using the latest LTS release

## [0.1.9](https://github.com/nationalarchives/docker/compare/v0.1.8...v0.1.9) - 2023-08-24

### Changed

- `tna-run` tries to use Django or Flask development servers if `$ENVIRONMENT == develop`, reverting to `gunicorn` if neither are available
- Updated Gunicorn to [21.2.0](https://github.com/benoitc/gunicorn/releases/tag/21.2.0)

## [0.1.8](https://github.com/nationalarchives/docker/compare/v0.1.7...v0.1.8) - 2023-08-22

### Changed

- Updated nvm to [v0.39.5](https://github.com/nvm-sh/nvm/releases/tag/v0.39.5)

## [0.1.7](https://github.com/nationalarchives/docker/compare/v0.1.6...v0.1.7) - 2023-08-22

### Changed

- Updated Poetry to [v1.6.1](https://github.com/python-poetry/poetry/releases/tag/1.6.1)

## [0.1.6](https://github.com/nationalarchives/docker/compare/v0.1.5...v0.1.6) - 2023-08-21

### Added

- Installed `build-essential` in `tna-python` to allow building of Node versions in nvm with GCC (GNU Compiler Collection)

### Changed

- Updated Poetry to [v1.6.0](https://github.com/python-poetry/poetry/releases/tag/1.6.0)

### Fixed

- Scripts exit immediately if any command or pipeline returns a non-zero exit status (`set -e`)
- Changed all exit codes to `1`
- `collectstatic` Django function on build won't error if `django.contrib.staticfiles` is not defined in `INSTALLED_APPS`
- Explicitly set `$NVM_DIR` following [nvm v0.39.4](https://github.com/nvm-sh/nvm/releases/tag/v0.39.4)

## [0.1.5](https://github.com/nationalarchives/docker/compare/v0.1.4...v0.1.5) - 2023-08-16

### Changed

- Updated nvm to [v0.39.4](https://github.com/nvm-sh/nvm/releases/tag/v0.39.4)

## [0.1.4](https://github.com/nationalarchives/docker/compare/v0.1.3...v0.1.4) - 2023-08-15

### Added

- Support for `linux/amd64` and `linux/arm64` base images

## [0.1.3](https://github.com/nationalarchives/docker/compare/v0.1.2...v0.1.3) - 2023-08-09

### Added

- Initial release of `tna-python-django` Docker image, ready for testing with services in beta
- Added support for `TIMEOUT` and `KEEP_ALIVE`

## Changed

- Node scripts are now run through `tna-node`
- Updated default number of workers and threads

## Fixed

- More stable build and run scripts in `tna-build` and `tna-run` with quotes around environment variables, tested with [ShellCheck](https://www.shellcheck.net/)

## [0.1.2](https://github.com/nationalarchives/docker/releases/tag/v0.1.2) - 2023-08-07

### Added

- Initial release of `tna-python` Docker image, ready for testing with services in beta
