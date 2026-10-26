.PHONY: install test retest coverage release format lint

install:
	uv sync

test:
	uv run pytest

retest:
	uv run pytest -vvv --lf

coverage:
	uv run coverage run -m pytest
	uv run coverage report -m --include="src/*"

release:
	rm -rf dist/*
	uv build

format:
	uv run ruff format src tests
	uv run ruff check --fix src tests

lint:
	uv run ruff format --check src tests
	uv run ruff check src tests
