.PHONY: install run format lint test

VERSION := $(shell git rev-parse --short=8 HEAD)


install:
	poetry install

run:
	gunicorn --reload -c gunicornconfig.py example_app.__main__:app

format:
	ruff --fix src tests
	black src tests

lint:
	ruff src tests || exit 1
	mypy src tests || exit 1
	black --check --diff src tests || exit 1

test: 
	coverage run -m pytest src tests
	coverage combine
	coverage report
	coverage xml