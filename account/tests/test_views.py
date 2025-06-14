# accounts/tests/test_auth.py

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class AuthTests(APITestCase):

    def setUp(self):
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "StrongPass123!",
            "password2": "StrongPass123!"
        }

    def test_signup_success(self):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "User registered successfully")
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_signup_password_mismatch(self):
        bad_data = self.user_data.copy()
        bad_data['password2'] = "WrongPass123!"
        response = self.client.post(self.signup_url, bad_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)

    def test_signup_existing_user(self):
        self.client.post(self.signup_url, self.user_data)
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data or "email" in response.data)

    def test_login_success(self):
        # First, register the user
        self.client.post(self.signup_url, self.user_data)
        login_data = {
            "username": self.user_data["username"],
            "password": self.user_data["password"]
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_invalid_credentials(self):
        login_data = {
            "username": "nonexistent",
            "password": "badpass"
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response.data)
