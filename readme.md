# ofmt

[![Lint](https://github.com/jncraton/ofmt/actions/workflows/lint.yml/badge.svg)](https://github.com/jncraton/ofmt/actions/workflows/lint.yml)
[![Test](https://github.com/jncraton/ofmt/actions/workflows/test.yml/badge.svg)](https://github.com/jncraton/ofmt/actions/workflows/test.yml)
[![Release](https://github.com/jncraton/ofmt/actions/workflows/release.yml/badge.svg)](https://github.com/jncraton/ofmt/actions/workflows/release.yml)
[![PyPI](https://img.shields.io/pypi/v/ofmt)](https://pypi.org/project/ofmt/)

Omni formatter. A formatter for everything.

## Usage

Format specific files:

```sh
uvx ofmt {files}
```

Walk the current working directory:

```sh
uvx ofmt
```

## Formatters

extension | formatter
----------|-----------
c, h, cpp, cc | clang-format
js, ts, jsx, tsx, html, css, json, jsonc | biome
md, yaml, yml | prettier
toml | taplo
sh, bash | shfmt
sql | sqlfluff
py | black

Formatters are downloaded as needed. A bundled `.prettierrc.json` is used when no project-level prettier config is found.
