from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from scavengerhunts.models import ScavengerHunt
from currentscavengerhunts.models  import CurrentScavengerHunt
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class CurrentScavengerHuntEndpointTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@email.com', password='password')
        self.token = Token.objects.get(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.scavenger_hunt_1 = self.user.scavengerhunt_set.create(name="scavenger hunt", description="tour denver's best speakeasies")
        self.scavenger_hunt_2 = self.user.scavengerhunt_set.create(name="scavenger hunt 2", description="yarg")


    def test_scavenger_hunt_create_endpoint(self):
        old_count = len(CurrentScavengerHunt.objects.all())

        data = { 'scavenger_hunt_id': 1 }

        response = self.client.post('/api/v1/current_scavenger_hunts/', data, format='json')

        new_count = len(CurrentScavengerHunt.objects.all())

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(new_count, 1)

    def test_scavenger_hunt_create_endpoint_no_corresponding_scavenger_hunt(self):
        old_count = len(CurrentScavengerHunt.objects.all())

        data = { 'scavenger_hunt_id': 3, 'random_field': 0 }

        response = self.client.post('/api/v1/current_scavenger_hunts/', data, format='json')

        new_count = len(CurrentScavengerHunt.objects.all())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(old_count, new_count)
        self.assertEqual(new_count, 0)

    def test_scavenger_hunt_index_endpoint(self):
        CurrentScavengerHunt.objects.create(scavenger_hunt_id=1, user_id=1)
        CurrentScavengerHunt.objects.create(scavenger_hunt_id=2, user_id=1)
        CurrentScavengerHunt.objects.create(scavenger_hunt_id=1, user_id=2)

        response = self.client.get('/api/v1/current_scavenger_hunts/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["scavenger_hunt_id"], 1)
        self.assertEqual(response.data[0]["user_id"], 1)
        self.assertEqual(response.data[1]["scavenger_hunt_id"], 2)
        self.assertEqual(response.data[1]["user_id"], 1)
