SHELL := /bin/bash

MAKEFLAGS := --silent --no-print-directory

.PHONY: help

.DEFAULT_GOAL := help

help:
   @echo "Please use 'make <target>' where <target> is one of"
   @awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z\._-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:
    pipenv install

activate:
    pipenv shell

run:
    python manage.py runserver

migration:
    python manage.py makemigrations

migrate:
    python manage.py migrate

superuser:
    python manage.py createsuperuser

heroku:
    git push heroku master

# target: test - calls the "test" django command
test:
	django-admin.py test --settings=$(TEST_SETTINGS)

# target: clean - remove all ".pyc" files
clean:
	django-admin.py clean_pyc --settings=$(SETTINGS)

# target: update - install (and update) pip requirements
update:
	pip install -U -r requirements.pip

# target: collect - calls the "collectstatic" django command
collect:
	django-admin.py collectstatic --settings=$(SETTINGS) --noinput