SHELL := /bin/bash

MAKEFLAGS := --silent --no-print-directory

.PHONY: help

.DEFAULT_GOAL := help

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z\._-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

r: run
run: ## runs django local server, alias r
	python3 manage.py runserver

mn: migration
migration: ## performs db migrations, alias mn
	python3 manage.py makemigrations

m: migrate
migrate: ## performs migrate on db, alias m
	python3 manage.py migrate

su: superuser
superuser: ## creates django app superuser, alias su
	python3 manage.py createsuperuser

hk: heroku
heroku: ## push to heroku, alias hk
	git push heroku master

# target: test - calls the "test" django command
t: test
test: ## run django tests
	python3 manage.py test

c: clean
clean: ## target: clean - remove all ".pyc" files, alias c
	django-admin.py clean_pyc --settings=$(SETTINGS)

i: update
update: ## target: update - install (and update) pip requirements, alias i
	pip3 install -U -r requirements.txt

l: lint
lint:
	pip3 install flake8
	flake8 .

collect: ## target: collect - calls the "collectstatic" django command
	django-admin.py collectstatic --settings=$(SETTINGS) --noinput
