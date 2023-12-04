# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/nationalarchives/docker/compare/v0.1.11...HEAD)

### Added
### Changed

- Updated Base Docker image from `python:3.11-slim` to `python:3.12-slim-bookworm`

### Deprecated
### Removed
### Fixed
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
