help:
	@echo "help  -- print this help"
	@echo "start -- start docker stack"
	@echo "stop  -- stop docker stack"
	@echo "ps    -- show status"
	@echo "build  -- build image"
	@echo "clean -- clean all artifacts"
	@echo "test  -- run tests using docker"
	@echo "dockershell -- run bash inside docker"

build:
	docker-compose build {{cookiecutter.project_name}}

start:
	docker-compose up -d {{cookiecutter.project_name}}

logs:
	docker-compose logs -f --tail=30 {{cookiecutter.project_name}}

up:
	docker-compose up {{cookiecutter.project_name}}

stop:
	docker-compose stop

ps:
	docker-compose ps

clean: stop
	docker-compose rm --force -v

only_test:
	docker-compose run --rm {{cookiecutter.project_name}} pytest -s --disable-pytest-warnings

covered_test:
	docker-compose run --rm {{cookiecutter.project_name}} pytest --cov=. --cov-config setup.cfg --disable-pytest-warnings

pep8:
	docker-compose run --rm {{cookiecutter.project_name}} flake8

test: pep8 covered_test

dockershell:
	docker-compose run --rm {{cookiecutter.project_name}} /bin/bash

shell_plus:
	docker-compose run --rm {{cookiecutter.project_name}} ipython

main:
	docker-compose run --rm {{cookiecutter.project_name}} python __main__.py

token:
	docker-compose run --rm {{cookiecutter.project_name}} python server.py

only_travis_test:
	docker-compose -f docker-compose.travis.yml run --rm {{cookiecutter.project_name}} pytest --cov=. --cov-config setup.cfg --disable-pytest-warnings

travis-test: pep8 only_travis_test

kill_docker:
	docker kill $(docker ps -q)

clean-python:
	rm -fr build
	rm -fr dist
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;

.PHONY: help start stop ps clean test dockershell shell_plus only_test pep8 clean-python
