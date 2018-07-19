from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
# from .models, import User

class UserModelTestCase(TestCase):

    def setUp(self):
        self.email = "user@user.com"
        self.password = "encrypted_password"
        self.user = User(email=self.email, password=self.password)

    def test_model_can_create_a_user(self):
        old_count = User.objects.count()
        self.user.save
        new_count = User.objects.count()
        new_user = User.objects.first()

        self.assertNotEqual(old_count, new_count)
        self.assertEqual(new_count, 1)
        self.assertEqual(new_user.email, self.email)
        self.assertEqual(new_user.password, self.password)
