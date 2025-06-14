run:
	python manage.py runserver --settings=config.settings.local

test:
	pytest

migrate:
	python manage.py migrate --settings=config.settings.local

makemigrations:
	python manage.py makemigrations --settings=config.settings.local

dep-prod:
	pip-compile requirements/in/production.in -o requirements/production.txt

dep-ci:
	pip-compile requirements/in/ci.in -o requirements/ci.txt

install-local:
	python -m pip install -r requirements/local.txt

install-prod:
	python -m pip install -r requirements/local.txt

install-ci:
	python -m pip install -r requirements/ci.txt
