.PHONY: install format lint test build run-debug-server run run-docker

VERSION := $(shell git rev-parse --short=8 HEAD)

install:
	poetry install

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

build:
	docker build -t example-app .

run-debug-server:
	python src/example_app/__main__.py

run:
	gunicorn --reload -c gunicornconfig.py example_app.__main__:app

run-docker:
	docker run -p 5000:5000 example-app

