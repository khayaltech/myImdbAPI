
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegisterTest(APITestCase):

    def test_create_account(self):
        data={
            'username':'myusername',
            'email':'username@email.com',
            'password':'yourpassword',
            'password2':'yourpassword'
        }
        response=self.client.post(reverse('register'),data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginLogoutTest(APITestCase):
    
    def setUp(self):
        self.user=User.objects.create_user(username='username',password='mypassword')

    def test_login(self):
        data={
            'username':'username',
            'password':'mypassword'
        }
        response=self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_logout(self):
        token = Token.objects.get(user__username='username')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response=self.client.post(reverse('logout'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    