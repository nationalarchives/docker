# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/nationalarchives/docker/compare/v1.6.0...HEAD)

### Added

- Installed `libmagic-dev`

### Changed

- Updated Poetry to [2.3.1](https://github.com/python-poetry/poetry/releases/tag/2.3.1)
- Updated Black to [26.1.0](https://github.com/psf/black/releases/tag/26.1.0)
- Updated Django Debug Toolbar to [6.2.0](https://github.com/django-commons/django-debug-toolbar/releases/tag/6.2.0)
- Updated Gunicorn to [24.1.1](https://github.com/benoitc/gunicorn/releases/tag/24.1.1)
- Updated Prettier to [3.8.1](https://github.com/prettier/prettier/releases/tag/3.8.1)

### Deprecated
### Removed
### Fixed
### Security

## [1.6.0](https://github.com/nationalarchives/docker/compare/v1.5.0...v1.6.0) - 2026-01-16

### Added

- Container labels added for `uk.gov.nationalarchives.nodejs-version` and `uk.gov.nationalarchives.python-version`

### Changed

- Updated Stylelint to [17.0.0](https://github.com/stylelint/stylelint/releases/tag/17.0.0)
- Updated Prettier to [3.8.0](https://github.com/prettier/prettier/releases/tag/3.8.0)
- Updated stylelint-config-standard-scss to [17.0.0](https://github.com/stylelint-scss/stylelint-config-standard-scss/releases/tag/v17.0.0)
- Move Node.js dependencies for formatting to the `Dockerfile`

### Deprecated

- `ALLOW_INSECURE=true` is ignored in favour of `APPLICATION_PROTOCOL=http`
- `PORT` environment variable removed in favour of `APPLICATION_PORT`

### Fixed

- Healthcheck for HTTPS applications fixed

## [1.5.0](https://github.com/nationalarchives/docker/compare/v1.4.1...v1.5.0) - 2026-01-13

### Added

- In `tna-python`, if `ALLOW_INSECURE=true` and no SSL certificate files exist, a self-signed SSL is created and used on startup

### Changed

- Disable the ASGI lifespan protocol for Uvicorn when running `tna-asgi`

## [1.4.1](https://github.com/nationalarchives/docker/compare/v1.4.0...v1.4.1) - 2026-01-07

### Changed

- Skip `migrations` in the default `.isort.cfg`

## [1.4.0](https://github.com/nationalarchives/docker/compare/v1.3.0...v1.4.0) - 2026-01-07

### Added

- Added support for `.stylelintignore` (https://stylelint.io/user-guide/ignore-code/#files-entirely)

## [1.3.0](https://github.com/nationalarchives/docker/compare/v1.2.3...v1.3.0) - 2026-01-07

### Added

- Add a default `.prettierrc` which ignores all `*.html` files which is only used when there is no `.prettierrc` in the project root

### Changed

- Updated stylelint-order to [7.0.1](https://github.com/hudochenkov/stylelint-order/releases/tag/7.0.1)
- Updated Uvicorn to [0.40.0](https://github.com/encode/uvicorn/releases/tag/0.40.0)
- Made the installation of `stylelint` quiet when running `format`
- Updated Black profile to include Python 3.14
- Ignored more files as part of the default `.eslintrc.js`
- Ignored all compiled CSS files (`*.css`) as part of the default `.stylelintrc`
- Used `npm install` rather than `npx` for formatting dependencies for increased repeat performance

## [1.2.3](https://github.com/nationalarchives/docker/compare/v1.2.2...v1.2.3) - 2025-12-19

### Changed

- Disabled `djLint` formatting fixes

## [1.2.2](https://github.com/nationalarchives/docker/compare/v1.2.1...v1.2.2) - 2025-12-19

### Fixed

- Fixed broken `format` script in `tna-python-dev`

## [1.2.1](https://github.com/nationalarchives/docker/compare/v1.2.0...v1.2.1) - 2025-12-19

### Changed

- Disabled djHTML

## [1.2.0](https://github.com/nationalarchives/docker/compare/v1.1.0...v1.2.0) - 2025-12-17

### Changed

- Don't remove `.nvmrc`, `package.json` and `package-lock.json` on `tna-clean`
- Allow disabling of djLint and djHTML when `DISABLE_DJLINT=true`

## [1.1.0](https://github.com/nationalarchives/docker/compare/v1.0.0...v1.1.0) - 2025-12-15

### Added

- Added [djLint](https://github.com/djlint/djLint) and [DjHTML](https://github.com/rtts/djhtml) to `tna-python-dev` and run linting and formatting on `format` for HTML files (assuming Jinja2)

### Changed

- Ensure `POETRY_HOME` and `NVM_DIR` are always correctly set for the `app` user
- Removed conditional check for `.nvmrc` in `format` script

### Security

- Set a fixed `$UID` and `$GID` for the non-root `app` user
- Install a specific version of the Django Debug Toolbar

## [1.0.0](https://github.com/nationalarchives/docker/compare/v0.15.0...v1.0.0) - 2025-12-08

### Added

- You can now include a CA certificate when using SSL
- `tna-python-dev` includes `django-debug-toolbar` by default
- A new `tna-clean` script is available to allow you to clean up the image before the application is run and increase the security

### Changed

- Changed base image from `python:3.13-slim-bookworm` (Python 3.13 on Debian 12) to `python:3.14-slim-trixie` (Python 3.14 on Debian 13)
- `tna-python-dev` is now a drop-in replacement for `tna-python` to run and develop your application localy with the addition of the development scripts and features
- Updated the LTS version of NodeJS from `jod` to `krypton`
- Updated isort to [7.0.0](https://github.com/PyCQA/isort/releases/tag/7.0.0)
- Updated Uvicorn to [0.38.0](https://github.com/encode/uvicorn/releases/tag/0.38.0)
- Updated Black to [25.12.0](https://github.com/psf/black/releases/tag/25.12.0)
- Updated Prettier to [3.7.4](https://github.com/prettier/prettier/releases/tag/3.7.4)
- Updated Stylelint to [16.26.1](https://github.com/stylelint/stylelint/releases/tag/16.26.1)
- When using FastAPI, the entry point needs to be a file called `main.py`
- `NODE_ENV` is hardcoded to `production` in `tna-python` and `development` in `tna-python-dev`
- Running ESLint and matching no files does not produce an error (`--no-error-on-unmatched-pattern`)

### Deprecated

- `tna-python-root` image deprecated
- `tna-python-django`, `tna-python-django-root` and `tna-python-root` images deprecated - Django projects can now use `tna-python` and `tna-python-dev`
- `tna-run` script deprecated in favour of `tna-wsgi` and `tna-asgi`
- `RUNTIME` environment variable deprecated
- AWS CLI and Docker removed from `tna-python-dev`

### Removed

- Removed `uvicorn-worker` (Uvicorn worker for Gunicorn) - Uvicorn is now run separately from Gunicorn

## [0.15.0](https://github.com/nationalarchives/docker/compare/v0.14.0...v0.15.0) - 2025-10-06

### Changed

- Updated Stylelint to [16.25.0](https://github.com/stylelint/stylelint/releases/tag/16.25.0)
- Updated Poetry to [2.2.1](https://github.com/python-poetry/poetry/releases/tag/2.2.1)
- Updated stylelint-config-standard-scss to [16.0.0](https://github.com/stylelint-scss/stylelint-config-standard-scss/releases/tag/v16.0.0)
- Don't throw an error with stylelint if no files are found [`--allow-empty-input`](https://stylelint.io/user-guide/options/#allowemptyinput)
- Updated Black to [25.9.0](https://github.com/psf/black/releases/tag/25.9.0)
- Updated Uvicorn to [0.37.0](https://github.com/encode/uvicorn/releases/tag/0.37.0)
- Updated Uvicorn Worker to [0.4.0](https://github.com/Kludex/uvicorn-worker/releases/tag/0.4.0)
- Updated isort to [6.1.0](https://github.com/PyCQA/isort/releases/tag/6.1.0)

## [0.14.0](https://github.com/nationalarchives/docker/compare/v0.13.1...v0.14.0) - 2025-08-08

### Added

- New `checkformat` option in `dev` image which reports on but doesn't fix linting and formatting issues for use in CI/CD pipelines

### Changed

- Formatting runs Prettier, stylelint and eslint if there is a `.nvmrc` file rather than a `package.json` file present

### Security

- Updated `libsqlite3-0` to fix [CVE-2025-6965](https://nvd.nist.gov/vuln/detail/CVE-2025-6965)
- Updated `curl` and `libcurl4` to their latest respective versions

## [0.13.1](https://github.com/nationalarchives/docker/compare/v0.13.0...v0.13.1) - 2025-08-08

### Changed

- Updated Stylelint to [16.23.1](https://github.com/stylelint/stylelint/releases/tag/16.23.1)

## [0.13.0](https://github.com/nationalarchives/docker/compare/v0.12.0...v0.13.0) - 2025-08-07

### Changed

- Updated Poetry to [2.1.4](https://github.com/python-poetry/poetry/releases/tag/2.1.4)

## [0.12.0](https://github.com/nationalarchives/docker/compare/v0.11.1...v0.12.0) - 2025-08-01

### Changed

- Updated Stylelint to [16.23.0](https://github.com/stylelint/stylelint/releases/tag/16.23.0)
- Removed `-verbose` option from Black formatting when running `format`
- Change Prettier to only output reformatted files (`--list-different` flag)
- `tna-python-django` no longer runs migrations for develop runtimes on `tna-run`

## [0.11.1](https://github.com/nationalarchives/docker/compare/v0.11.0...v0.11.1) - 2025-07-04

### Changed

- Amended default flake8 config to not define a select list and ignore `E501` and `W503`

## [0.11.0](https://github.com/nationalarchives/docker/compare/v0.10.0...v0.11.0) - 2025-07-04

### Added

- AWS CLI (`2.27.45`) added to `tna-python-dev`

### Changed

- Updated Uvicorn to [0.35.0](https://github.com/encode/uvicorn/releases/tag/0.35.0)
- Updated Stylelint to [16.21.0](https://github.com/stylelint/stylelint/releases/tag/16.21.0)
- Updated stylelint-config-standard-scss to [15.0.1](https://github.com/stylelint-scss/stylelint-config-standard-scss/releases/tag/v15.0.1)
- Updated Prettier to [3.6.2](https://github.com/prettier/prettier/releases/tag/3.6.2)
- Update default Flake8 configuration to reinstate some ignored rules

### Removed

- Removed the default `manage.py` from `tna-python-django`

## [0.10.0](https://github.com/nationalarchives/docker/compare/v0.9.1...v0.10.0) - 2025-05-13

### Added

- Added `outdated` command to `tna-python-dev` to show outdated packages

### Changed

- Updated Stylelint to [16.19.1](https://github.com/stylelint/stylelint/releases/tag/16.19.1)
- Updated interval on healthcheck to 15 seconds
- Updated Poetry to [2.1.3](https://github.com/python-poetry/poetry/releases/tag/2.1.3)

### Deprecated

- Support for the `ENVIRONMENT` variable has been dropped in favour of `RUNTIME`

### Fixed

- Make `ALLOW_INSECURE` case-insensitive

## [0.9.1](https://github.com/nationalarchives/docker/compare/v0.9.0...v0.9.1) - 2025-04-28

### Security

- Version bump to include newer h11 `0.16.0` package to fix [CVE-2025-43859](https://nvd.nist.gov/vuln/detail/CVE-2025-43859)

## [0.9.0](https://github.com/nationalarchives/docker/compare/v0.8.0...v0.9.0) - 2025-04-24

### Added

- For `tna-python-django`, create a separate `migrate` script for applying database migrations
- Added a heathcheck for `dev` containers

### Changed

- The `ENVIRONMENT` variable has now changed to `RUNTIME` - both will still work for now but `ENVIRONMENT` will be deprecated in a future release
- Updated `curl` and `libcurl4` packages
- Updated Stylelint to [16.19.0](https://github.com/stylelint/stylelint/releases/tag/16.19.0)
- Updated Poetry to [2.1.2](https://github.com/python-poetry/poetry/releases/tag/2.1.2)
- Only run Django migrations automatically when `$RUNTIME` is set to `develop`
- Updated Uvicorn to [0.34.2](https://github.com/encode/uvicorn/releases/tag/0.34.2)
- Updated stylelint-order to [7.0.0](https://github.com/hudochenkov/stylelint-order/releases/tag/7.0.0)
- Updated nvm to [v0.40.3](https://github.com/nvm-sh/nvm/releases/tag/v0.40.3)

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
