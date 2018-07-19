from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UserModelTestCase(TestCase):

    def setUp(self):
        self.email = "user@user.com"
        self.password = "encrypted_password"
        self.user = User(email=self.email, password=self.password)

    def test_model_can_create_a_user(self):
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        new_user = User.objects.first()

        self.assertNotEqual(old_count, new_count)
        self.assertEqual(new_count, 1)
        self.assertEqual(new_user.email, self.email)
        self.assertEqual(new_user.password, self.password)

class UserEndpointsTesetCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.email = "user@user.com"
        self.password = "encrypted_password"
        self.user = User(email=self.email, password=self.password)

        self.email2 = "user2@user.com"
        self.password2 = "encrypted_password2"
        self.user2 = User(email=self.email2, password=self.password2)

        self.email3 = "user3@user.com"
        self.password3 = "encrypted_password3"
        self.post_params = {'user': {'email': self.email3, 'password': self.password3}}

    def test_user_create_endpoint(self):
        response = self.client.post('/api/v1/users/', {'user': {'email': self.email3, 'password': self.password3}}, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['user']['id'], 1)
        self.assertEqual(response.json()['user']['email'], self.email3)
        self.assertEqual(response.json()['user']['auth_token'], 'test')
