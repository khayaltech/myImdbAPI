from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class StreamPlatformTest(APITestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='myusername',password='mypassword')
        self.token=Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

    def test_streamplatform_create(self):
        data={
            'name':'Netflix',
            'about':'Netflix description',
            'website':'https://www.netflix.com/browse'
        }
        response=self.client.post(reverse('stream-list'),data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response=self.client.get(reverse('stream-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
