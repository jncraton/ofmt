# ofmt

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

### Usage

```sh
uvx ofmt {files}
```

or to walk the current working directory:

```sh
uvx ofmt
```
