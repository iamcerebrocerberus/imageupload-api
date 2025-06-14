run:
	python manage.py runserver --settings=config.settings.local

test:
	pytest

migrate:
	python manage.py migrate --settings=config.settings.local

makemigrations:
	python manage.py makemigrations --settings=config.settings.local
