SHELL := /bin/bash

help:
    @$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

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
