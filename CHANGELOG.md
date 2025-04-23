# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/nationalarchives/docker/compare/v0.8.0...HEAD)

### Added

- For `tna-python-django`, create a separate `migrate` script for applying database migrations

### Changed

- The `ENVIRONMENT` variable has now changed to `RUNTIME` - both will still work for now but `ENVIRONMENT` will be deprecated in a future release
- Updated `curl` and `libcurl4` packages
- Updated Stylelint to [16.19.0](https://github.com/stylelint/stylelint/releases/tag/16.19.0)
- Updated Poetry to [2.1.2](https://github.com/python-poetry/poetry/releases/tag/2.1.2)
- Only run Django migrations automatically when `$RUNTIME` is set to `develop`
- Updated Uvicorn to [0.34.2](https://github.com/encode/uvicorn/releases/tag/0.34.2)
- Updated stylelint-order to [7.0.0](https://github.com/hudochenkov/stylelint-order/releases/tag/7.0.0)

### Deprecated
### Removed
### Fixed
### Security

## [0.8.0](https://github.com/nationalarchives/docker/compare/v0.7.0...v0.8.0) - 2025-03-12

### Added

- Black target version `py313` added

### Changed

- Updated Stylelint to [16.15.0](https://github.com/stylelint/stylelint/releases/tag/16.15.0)
- Updated Black to [25.1.0](https://github.com/psf/black/releases/tag/25.1.0)
- Updated isort to [6.0.1](https://github.com/PyCQA/isort/releases/tag/6.0.1)
- Updated Prettier to [3.5.3](https://github.com/prettier/prettier/releases/tag/3.5.3)
- Updated nvm to [v0.40.2](https://github.com/nvm-sh/nvm/releases/tag/v0.40.2)

### Deprecated

- Black target version `py38` removed

## [0.7.0](https://github.com/nationalarchives/docker/compare/v0.6.0...v0.7.0) - 2025-01-13

### Added

- `. tna-npm` can be used to load nvm and install the required version

### Changed

- Changed Python line lengths from `80` to `88` (default for Black)

### Removed

- `staging` option removed from `ENVIRONMENT` - there is now only `production` and `develop`
- `welcome` script removed and added to the end of `dev`

### Fixed

- Only upgrade npm packages or try to build with `NPM_BUILD_COMMAND` if a `package.json` file exists

## [0.6.0](https://github.com/nationalarchives/docker/compare/v0.5.2...v0.6.0) - 2025-01-03

### Added

- Added `stylelint-order` for `stylelint`
- `manage` command added to `tna-python-django`
- The `upgrade` command in the dev container can now run separate upgrades with either `upgrade poetry` or `upgrade npm`

### Changed

- Installation of Python formatting and linting tools moved to `Dockerfile` so are available at startup of the dev image
- Updated `prettier`, `stylelint` and `stylelint-config-standard-scss` in `tna-python-dev`
- Updated Poetry to [1.8.5](https://github.com/python-poetry/poetry/releases/tag/1.8.5)
- Updated Stylelint to [16.12.0](https://github.com/stylelint/stylelint/releases/tag/16.12.0)
- Updated Uvicorn to [0.34.0](https://github.com/encode/uvicorn/releases/tag/0.34.0)
- Updated Uvicorn Worker to [0.3.0](https://github.com/Kludex/uvicorn-worker/releases/tag/0.3.0)

### Fixed

- Allow the `manage` command in the dev container to accept multiple arguments

## [0.5.2](https://github.com/nationalarchives/docker/compare/v0.5.1...v0.5.2) - 2024-12-04

### Changed

- Minor NodeJS version bump to `22.12`

## [0.5.1](https://github.com/nationalarchives/docker/compare/v0.5.0...v0.5.1) - 2024-11-19

### Added

- `git` is now available in `tna-python-dev`
- Ability to change port by specifying a `PORT` environment variable

### Changed

- Updated Uvicorn to [0.32.1](https://github.com/encode/uvicorn/releases/tag/0.32.1)

## [0.5.0](https://github.com/nationalarchives/docker/compare/v0.4.0...v0.5.0) - 2024-11-19

### Added

- SSL certificates must be generated and used on environments outside of production
- Docker added back into `tna-python-dev`
- `tna-python-dev` can now run custom scripts when mounted to `/home/app/.local/bin/tasks`

### Changed

- Set the `default` alias for nvm to `lts/jod`

### Removed

- Removed `lts/iron`

### Fixed

- Fixed the default NodeJS version in `tna-python-dev`

### Security

- Updated `curl` and `libcurl4` to `7.88.1-10+deb12u8` (fixes [CVE-2024-2004](https://avd.aquasec.com/nvd/2024/cve-2024-2004/), [CVE-2024-2398](https://avd.aquasec.com/nvd/2024/cve-2024-2398/) and [CVE-2024-7264](https://avd.aquasec.com/nvd/cve-2024-7264))

## [0.4.0](https://github.com/nationalarchives/docker/compare/v0.3.0...v0.4.0) - 2024-11-04

### Added

- Pre-installed the previous NodeJS LTS version as well as the latest
- Semantically versioned images get tagged with their major and minor versions as well as the full version number

### Changed

- Updated `black`, `flake8`, `prettier`, `stylelint`, `stylelint-config-standard-scss` and `stylelint-selector-bem-pattern` in the dev image
- Updated the LTS version of NodeJS from `iron` to `jod`

### Removed

- The dev image no longer contains `docker`

### Fixed

- Fixed the `rg.opencontainers.image.description` in the Django image

## [0.3.0](https://github.com/nationalarchives/docker/compare/v0.2.11...v0.3.0) - 2024-10-18

### Added

- Install Poetry `root` group during `tna-build` process in `tna-python-root` and `tna-python-django-root`

### Changed

- Updated Python to [3.13](https://www.python.org/downloads/release/python-3130/)
- Updated Poetry to [1.8.4](https://github.com/python-poetry/poetry/releases/tag/1.8.4)
- Updated Uvicorn to [0.32.0](https://github.com/encode/uvicorn/releases/tag/0.32.0)

## [0.2.11](https://github.com/nationalarchives/docker/compare/v0.2.10...v0.2.11) - 2024-10-11

### Changed

- Updated Uvicorn to [0.31.1](https://github.com/encode/uvicorn/releases/tag/0.31.1)

## [0.2.10](https://github.com/nationalarchives/docker/compare/v0.2.9...v0.2.10) - 2024-09-02

### Changed

- Install Poetry `dev` group during startup of `tna-python-dev`
- Updated Uvicorn to [0.30.6](https://github.com/encode/uvicorn/releases/tag/0.30.6)
- Updated nvm to [v0.40.1](https://github.com/nvm-sh/nvm/releases/tag/v0.40.1)
- Updated Gunicorn to [23.0.0](https://github.com/benoitc/gunicorn/releases/tag/23.0.0)

## [0.2.9](https://github.com/nationalarchives/docker/compare/v0.2.8...v0.2.9) - 2024-07-18

### Fixed

- Make `SECRET_KEY` optional (missed from last release)

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
