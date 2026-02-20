import shutil
import subprocess
import sys
from pathlib import Path


def runner():
    """
    >>> runner() in ('uvx', 'pipx')
    True
    """
    return "uvx" if shutil.which("uvx") else "pipx"


def node_runner():
    """
    >>> node_runner() in ('pnpm dlx', 'npx')
    True
    """
    return "pnpm dlx" if shutil.which("pnpm") else "npx"


FORMATTERS = {
    "c": "clang",
    "h": "clang",
    "cpp": "clang",
    "cc": "clang",
    "js": "prettier",
    "html": "prettier",
    "css": "prettier",
    "py": "black",
}


IGNORED_DIRS = {
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
}


def ignored(path):
    """
    >>> ignored(Path('.git/config'))
    True
    >>> ignored(Path('node_modules/foo.js'))
    True
    >>> ignored(Path('src/main.py'))
    False
    """
    for part in path.parts:
        if part.startswith(".") or part in IGNORED_DIRS:
            return True
    return False


def collect_files(paths):
    """
    >>> collect_files([]) == []
    True
    """
    result = []
    for p in paths:
        path = Path(p)
        if path.is_dir():
            for f in path.rglob("*"):
                if f.is_file() and not ignored(f):
                    result.append(f)
        else:
            result.append(path)
    return result


def group_by_formatter(files):
    """
    >>> groups = group_by_formatter([Path('a.py'), Path('b.js')])
    >>> sorted(groups.keys())
    ['black', 'prettier']
    """
    groups = {}
    for f in files:
        ext = f.suffix.lstrip(".")
        if ext not in FORMATTERS:
            continue
        kind = FORMATTERS[ext]
        groups.setdefault(kind, []).append(f)
    return groups


def prettier_config():
    """
    >>> isinstance(prettier_config(), list)
    True
    """
    result = subprocess.run(
        ["npx", "prettier", "--find-config-path", "."],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0 and result.stdout.strip():
        return []
    bundled = Path(__file__).parent / ".prettierrc.json"
    return ["--config", str(bundled)]

    if not files:
        return
    if kind == "black":
        subprocess.run([runner(), "black"] + [str(f) for f in files], check=True)
    elif kind == "prettier":
        subprocess.run(
            node_runner().split()
            + ["prettier", "--write"]
            + prettier_config()
            + [str(f) for f in files],
            check=True,
        )
    elif kind == "clang":
        subprocess.run(
            [runner(), "clang-format", "-i"] + [str(f) for f in files], check=True
        )


def main():
    """
    >>> main is not None
    True
    """
    args = sys.argv[1:]
    if args:
        raw_files = collect_files(args)
    else:
        raw_files = collect_files([Path(".")])

    groups = group_by_formatter(raw_files)
    for kind, files in groups.items():
        run_formatter(kind, files)


if __name__ == "__main__":
    main()
