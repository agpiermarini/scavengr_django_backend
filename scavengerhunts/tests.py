from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from scavengerhunts.models import ScavengerHunt
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ScavengerHuntEndpointTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@email.com', password='password')
        self.user2 = User.objects.create(username='testuser2', email='test2@email.com', password='password')
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

    def test_scavenger_hunt_update_endpoint_put_request(self):
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

    def test_scavenger_hunt_update_endpoint_put_request_no_name(self):
        scavenger_hunt = ScavengerHunt.objects.create(id=1, name="old_name", description="old_description", user_id=self.user.id)

        data = {
                'name': "",
                'description': self.description
                }

        response = self.client.put('/api/v1/scavenger_hunts/1', data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_scavenger_hunt_update_endpoint_put_request_no_description(self):
        scavenger_hunt = ScavengerHunt.objects.create(id=1, name="old_name", description="old_description", user_id=self.user.id)

        data = {
                'name': self.name,
                'description': ""
                }

        response = self.client.put('/api/v1/scavenger_hunts/1', data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_scavenger_hunt_update_endpoint_put_request_no_corresponding_record(self):
        data = {
                'name': self.name,
                'description': self.description
                }

        response = self.client.put('/api/v1/scavenger_hunts/1', data, format='json')

        self.assertEqual(response.status_code, 404)

    def test_scavenger_hunt_update_endpoint_patch_request(self):
        scavenger_hunt = ScavengerHunt.objects.create(id=1, name="old_name", description="old_description", user_id=self.user.id)

        data = {
                'name': self.name,
                'description': self.description
                }

        response = self.client.patch('/api/v1/scavenger_hunts/1', data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['name'], self.name)
        self.assertEqual(response.data['description'], self.description)
        self.assertEqual(response.data['user_id'], self.user.id)
        self.assertEqual(response.data['username'], self.user.username)

    def test_scavenger_hunt_update_endpoint_patch_request_no_name(self):
        scavenger_hunt = ScavengerHunt.objects.create(id=1, name="old_name", description="old_description", user_id=self.user.id)

        data = {
                'name': "",
                'description': self.description
                }

        response = self.client.patch('/api/v1/scavenger_hunts/1', data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_scavenger_hunt_update_endpoint_patch_request_no_description(self):
        scavenger_hunt = ScavengerHunt.objects.create(id=1, name="old_name", description="old_description", user_id=self.user.id)

        data = {
                'name': self.name,
                'description': ""
                }

        response = self.client.patch('/api/v1/scavenger_hunts/1', data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_scavenger_hunt_update_endpoint_patch_request_no_corresponding_record(self):
        data = {
                'name': self.name,
                'description': self.description
                }

        response = self.client.patch('/api/v1/scavenger_hunts/1', data, format='json')

        self.assertEqual(response.status_code, 404)

    def test_scavenger_hunt_show_endpoint(self):
        scavenger_hunt = ScavengerHunt.objects.create(id=1, name=self.name, description=self.description, user_id=self.user.id)
        response = self.client.get('/api/v1/scavenger_hunts/1')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['name'], self.name)
        self.assertEqual(response.data['description'], self.description)
        self.assertEqual(response.data['user_id'], self.user.id)
        self.assertEqual(response.data['username'], self.user.username)

    def test_scavenger_hunt_show_endpoint_no_corresponding_record(self):
        response = self.client.get('/api/v1/scavenger_hunts/1')

        self.assertEqual(response.status_code, 404)

    def test_scavenger_hunt_index_endpoint(self):
        ScavengerHunt.objects.create(id=1, name=self.name, description=self.description, user_id=self.user.id)
        ScavengerHunt.objects.create(id=2, name="second_hunt", description="second_description", user_id=self.user.id)
        ScavengerHunt.objects.create(id=3, name="third_hunt", description="third_description", user_id=self.user2.id)

        response = self.client.get('/api/v1/scavenger_hunts/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
        self.assertEqual(response.json()[0]['id'], 1)
        self.assertEqual(response.json()[0]['name'], self.name)
        self.assertEqual(response.json()[0]['description'], self.description)
        self.assertEqual(response.json()[0]['user_id'], self.user.id)
        self.assertEqual(response.json()[0]['username'], self.user.username)
        self.assertEqual(response.json()[1]['id'], 2)
        self.assertEqual(response.json()[1]['name'], "second_hunt")
        self.assertEqual(response.json()[1]['description'], "second_description")
        self.assertEqual(response.json()[1]['user_id'], self.user.id)
        self.assertEqual(response.json()[1]['username'], self.user.username)
        self.assertEqual(response.json()[2]['id'], 3)
        self.assertEqual(response.json()[2]['name'], "third_hunt")
        self.assertEqual(response.json()[2]['description'], "third_description")
        self.assertEqual(response.json()[2]['user_id'], self.user2.id)
        self.assertEqual(response.json()[2]['username'], self.user2.username)

    def test_scavenger_hunt_delete_endpoint(self):
        scavenger_hunt1 = ScavengerHunt.objects.create(id=1, name=self.name, description=self.description, user_id=self.user.id)
        scavenger_hunt2 = ScavengerHunt.objects.create(id=2, name=self.name, description=self.description, user_id=self.user.id)

        self.assertEqual(len(ScavengerHunt.objects.all()), 2)

        response = self.client.delete('/api/v1/scavenger_hunts/1')

        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(ScavengerHunt.objects.all()), 1)

    def test_scavenger_hunt_show_endpoint_no_corresponding_record(self):
        response = self.client.delete('/api/v1/scavenger_hunts/3')

        self.assertEqual(response.status_code, 404)

    def test_user_specific_scavenger_hunt_index_endpoint(self):
        ScavengerHunt.objects.create(id=1, name=self.name, description=self.description, user_id=self.user.id)
        ScavengerHunt.objects.create(id=2, name="second_hunt", description="second_description", user_id=self.user.id)
        ScavengerHunt.objects.create(id=3, name="third_hunt", description="third_description", user_id=self.user2.id)
        response = self.client.get('/api/v1/users/1/scavenger_hunts/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['id'], 1)
        self.assertEqual(response.json()[0]['name'], self.name)
        self.assertEqual(response.json()[0]['description'], self.description)
        self.assertEqual(response.json()[0]['user_id'], self.user.id)
        self.assertEqual(response.json()[0]['username'], self.user.username)
        self.assertEqual(response.json()[1]['id'], 2)
        self.assertEqual(response.json()[1]['name'], "second_hunt")
        self.assertEqual(response.json()[1]['description'], "second_description")
        self.assertEqual(response.json()[1]['user_id'], self.user.id)
        self.assertEqual(response.json()[1]['username'], self.user.username)
