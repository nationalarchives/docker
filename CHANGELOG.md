# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/nationalarchives/docker/compare/v0.1.5...HEAD)

### Added
### Changed

- Updated Poetry to [v1.6.0](https://github.com/python-poetry/poetry/releases/tag/1.6.0)

### Deprecated
### Removed
### Fixed

- Scripts exit immediately if any command or pipeline returns a non-zero exit status

### Security

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
