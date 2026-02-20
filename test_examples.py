import shutil
import subprocess
import tempfile
from pathlib import Path

EXAMPLES = Path(__file__).parent / "examples"


def run_ofmt(tmp):
    subprocess.run(["uv", "run", "--with-editable", ".", "ofmt", str(tmp)], check=True)


def test_c():
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(EXAMPLES / "example.c", tmp)
        run_ofmt(tmp)
        result = (Path(tmp) / "example.c").read_text()
    assert "int main()" in result
    assert "int x = 1;" in result


def test_js():
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(EXAMPLES / "example.js", tmp)
        run_ofmt(tmp)
        result = (Path(tmp) / "example.js").read_text()
    assert "function hello(x, y)" in result


def test_ts():
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(EXAMPLES / "example.ts", tmp)
        run_ofmt(tmp)
        result = (Path(tmp) / "example.ts").read_text()
    assert "function hello(x: number, y: number)" in result


def test_css():
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(EXAMPLES / "example.css", tmp)
        run_ofmt(tmp)
        result = (Path(tmp) / "example.css").read_text()
    assert "color: red;" in result


def test_json():
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(EXAMPLES / "example.json", tmp)
        run_ofmt(tmp)
        result = (Path(tmp) / "example.json").read_text()
    assert '"description": "test"' in result


def test_py():
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(EXAMPLES / "example.py", tmp)
        run_ofmt(tmp)
        result = (Path(tmp) / "example.py").read_text()
    assert "x = 1\n" in result
    assert "y = 2\n" in result


def test_toml():
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(EXAMPLES / "example.toml", tmp)
        run_ofmt(tmp)
        result = (Path(tmp) / "example.toml").read_text()
    assert 'name = "ofmt"' in result
    assert 'version = "1"' in result


def test_sh():
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(EXAMPLES / "example.sh", tmp)
        run_ofmt(tmp)
        result = (Path(tmp) / "example.sh").read_text()
    assert '[ "$1" = "hello" ]' in result


def test_yaml():
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(EXAMPLES / "example.yaml", tmp)
        run_ofmt(tmp)
        result = (Path(tmp) / "example.yaml").read_text()
    assert "key: value\n" in result
    assert "other: 123\n" in result


def test_sql():
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(EXAMPLES / "example.sql", tmp)
        run_ofmt(tmp)
        result = (Path(tmp) / "example.sql").read_text()
    assert "select" in result
    assert "SELECT" not in result
