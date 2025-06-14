# Simple Image Upload API

This is a **simple but robust backend API** built with Django and Django REST Framework (DRF), allowing authenticated users to upload images and retrieve optional AI-based analysis. Images are securely stored in the cloud using **Amazon S3**.


## ✨ Features

- 📸 Upload images via a RESTful API
- 🔐 JWT-based user authentication
- 👤 Each image is associated with a user account
- 🧠 Optional AI image analysis (e.g., OCR, object detection)
- ☁️ Image storage powered by AWS S3
- 🧪 TDD-based test suite using `django.test.TestCas


## Tech Stack
- Django 5, Django Rest Framework
- JWT
- AWS S3 via `django-storages`, `boto3`
- PostgreSQL
