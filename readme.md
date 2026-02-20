# ofmt

[![Lint](https://github.com/jncraton/ofmt/actions/workflows/lint.yml/badge.svg)](https://github.com/jncraton/ofmt/actions/workflows/lint.yml)
[![Test](https://github.com/jncraton/ofmt/actions/workflows/test.yml/badge.svg)](https://github.com/jncraton/ofmt/actions/workflows/test.yml)
[![Release](https://github.com/jncraton/ofmt/actions/workflows/release.yml/badge.svg)](https://github.com/jncraton/ofmt/actions/workflows/release.yml)
[![PyPI](https://img.shields.io/pypi/v/ofmt)](https://pypi.org/project/ofmt/)

Omni formatter. A formatter for everything.

## Formatters

This project includes and calls the following formatters as appropriate:

extension | formatter
----------|-----------
c | clang-format -i {files}
h | clang-format -i {files}
cpp | clang-format -i {files}
cc | clang-format -i {files}
js | npx prettier --write {files}
html | npx prettier --write {files}
css | npx prettier --write {files}
py | uvx black

Most formatters are downloaded as needed by their respective package managers. The clang-format binary is included as part of the resources of this package and used from there automatically.

### Usage

```sh
uvx ofmt {files}
```

or to walk the current working directory:

```sh
uvx ofmt
```
