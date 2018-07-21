from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from scavengerhunts.models import ScavengerHunt
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ScavengerHuntEndpointTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@email.com', password='password')
        self.token = Token.objects.get(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.name = "scavenger hunt"
        self.description = "tour denver's best speakeasies"

    def test_scavenger_hunt_create_endpoint(self):
        data = {
                'name': self.name,
                'description': self.description
                }

        response = self.client.post('/api/v1/scavenger_hunts/', data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['name'], self.name)
        self.assertEqual(response.data['description'], self.description)
        self.assertEqual(response.data['user_id'], self.user.id)
        self.assertEqual(response.data['username'], self.user.username)

    def test_scavenger_hunt_create_endpoint_no_name(self):
        data = {
                'name': "",
                'description': self.description
                }

        response = self.client.post('/api/v1/scavenger_hunts/', data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_scavenger_hunt_create_endpoint_no_description(self):
        data = {
                'name': self.name,
                'description': ""
                }

        response = self.client.post('/api/v1/scavenger_hunts/', data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_scavenger_hunt_update_endpoint(self):
        scavenger_hunt = ScavengerHunt.objects.create(id=1, name="old_name", description="old_description", user_id=self.user.id)

        data = {
                'name': self.name,
                'description': self.description
                }

        response = self.client.put('/api/v1/scavenger_hunts/1', data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['name'], self.name)
        self.assertEqual(response.data['description'], self.description)
        self.assertEqual(response.data['user_id'], self.user.id)
        self.assertEqual(response.data['username'], self.user.username)

    def test_scavenger_hunt_update_endpoint_no_name(self):
        data = {
                'name': "",
                'description': self.description
                }

        response = self.client.put('/api/v1/scavenger_hunts/1', data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_scavenger_hunt_update_endpoint_no_description(self):
        data = {
                'name': self.name,
                'description': ""
                }

        response = self.client.put('/api/v1/scavenger_hunts/1', data, format='json')

        self.assertEqual(response.status_code, 400)
