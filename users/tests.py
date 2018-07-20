from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

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
