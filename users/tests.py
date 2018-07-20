from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserModelTestCase(TestCase):

    def setUp(self):
        self.username = "username"
        self.email = "username@email.com"
        self.password = "password"


    def test_model_can_create_a_user(self):
        old_count = User.objects.count()
        user = User.objects.create_user(username=self.username, email=self.email, password=self.password)
        new_count = User.objects.count()

        self.assertNotEqual(old_count, new_count)
        self.assertEqual(new_count, 1)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertNotEqual(user.password, self.password)

class UserEndpointTestCase(TestCase):

    def setUp(self):
        self.username = "username"
        self.email = "username@email.com"
        self.password = "password"

    def test_user_create_endpoint(self):
        data = {
                 'username': self.username,
                 'email': self.email,
                 'password': self.password
               }

        response = self.client.post('/api/v1/users/', data, format='json')

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], self.username)
        self.assertEqual(response.data['email'], self.email)
        self.assertFalse('password' in response.data)


        user = User.objects.last()
        token = Token.objects.get(user=user)
        self.assertEqual(response.data['token'], token.key)

    def test_user_create_endpoint_preexising_username(self):
        User.objects.create_user(username=self.username, email=self.email, password=self.password)
        data = {
                 'username': self.username,
                 'email': 'test2@email.com',
                 'password': self.password
               }

        response = self.client.post('/api/v1/users/', data, format='json')

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_create_endpoint_no_username(self):
        data = {
                 'username': '',
                 'email': self.email,
                 'password': self.password
               }

        response = self.client.post('/api/v1/users/', data, format='json')

        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_create_endpoint_username_too_long(self):
        data = {
                 'username': 't'*26,
                 'email': self.email,
                 'password': self.password
               }

        response = self.client.post('/api/v1/users/', data, format='json')

        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_create_endpoint_preexisting_email(self):
        User.objects.create_user(username=self.username, email=self.email, password=self.password)
        data = {
                 'username': 'uniqueusername',
                 'email': self.email,
                 'password': self.password
               }

        response = self.client.post('/api/v1/users/', data, format='json')

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_create_endpoint_invalid_email(self):
        data = {
                 'username': self.username,
                 'email': 'invalidemailformat',
                 'password': self.password
               }

        response = self.client.post('/api/v1/users/', data, format='json')

        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_create_endpoint_no_email(self):
        data = {
                 'username': self.username,
                 'email': '',
                 'password': self.password
               }

        response = self.client.post('/api/v1/users/', data, format='json')

        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_create_endpoint_no_password(self):
        data = {
                 'username': self.username,
                 'email': self.email,
                 'password': ''
               }

        response = self.client.post('/api/v1/users/', data, format='json')

        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_create_endpoint_password_shorter_than_8_chars(self):
        data = {
                 'username': self.username,
                 'email': self.email,
                 'password': '2short'
               }

        response = self.client.post('/api/v1/users/', data, format='json')

        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
