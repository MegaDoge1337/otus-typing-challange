.PHONY: typing, lint, format, import-sort


typing:
	poetry run mypy .

lint:
	poetry run ruff check

format:
	poetry run black .

import-sort:
	poetry run isort .
