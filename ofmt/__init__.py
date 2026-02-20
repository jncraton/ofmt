import subprocess
import sys
from pathlib import Path

FORMATTERS = {
    "c": ("clang", ["clang-format", "-i"]),
    "h": ("clang", ["clang-format", "-i"]),
    "cpp": ("clang", ["clang-format", "-i"]),
    "cc": ("clang", ["clang-format", "-i"]),
    "js": ("prettier", ["npx", "prettier", "--write"]),
    "html": ("prettier", ["npx", "prettier", "--write"]),
    "css": ("prettier", ["npx", "prettier", "--write"]),
    "py": ("black", None),
}


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
                if f.is_file():
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
        kind, _ = FORMATTERS[ext]
        groups.setdefault(kind, []).append(f)
    return groups


def run_formatter(kind, files):
    if not files:
        return
    if kind == "black":
        subprocess.run(["uvx", "black"] + [str(f) for f in files], check=True)
    elif kind == "prettier":
        subprocess.run(
            ["npx", "prettier", "--write"] + [str(f) for f in files], check=True
        )
    elif kind == "clang":
        subprocess.run(
            ["uvx", "clang-format", "-i"] + [str(f) for f in files], check=True
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
