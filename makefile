.PHONY: changelog.md

lint:
	uvx black --check ofmt/

format:
	uvx black ofmt/

test:
	uv run --with pytest python -m pytest --doctest-modules ofmt/

changelog.md:
	uvx git-cliff -o changelog.md

upload: changelog.md
	uv build
	uv publish

clean:
	rm -rf .pytest_cache __pycache__ ofmt/__pycache__ dist/ changelog.md .venv .ruff_cache ofmt/__pycache__
