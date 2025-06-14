# Use the official Python slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=config.settings.production

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && apt-get clean

# Set work directory
WORKDIR /code

# Copy and install dependencies
COPY requirements/production.txt /code/requirements/production.txt
RUN pip install --upgrade pip
RUN pip install -r requirements/production.txt

# Copy project files
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the app with Gunicorn on Fly's expected port
CMD ["gunicorn", "--bind", ":8080", "--workers", "2", "config.wsgi"]
