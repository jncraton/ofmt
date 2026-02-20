lint:
	uvx black --check ofmt/

format:
	uvx black ofmt/

test:
	uv run --with pytest python -m pytest --doctest-modules ofmt/

clean:
	rm -rf .pytest_cache __pycache__ ofmt/__pycache__
