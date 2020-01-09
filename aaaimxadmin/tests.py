from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password


class UserTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('', include('aaaimxadmin.urls')),
    ]

    def test_get_users(self):
        """
        Ensure we have users created.
        """
        User.objects.create(
            username='migrated@jambonsw.com',
            password=make_password('s3cr3tp4ssw0rd!'),
            is_superuser=True
        )
        url = reverse('user-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_create_user(self):
        """
        Should return 403 due to not authentication provided.
        """
        url = reverse('user-list')
        data = {'username': 'Admin'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_incorrect_credentials(self):
        """
        Should return 401 due to invalid credentials.
        """
        url = reverse('token_obtain_pair')
        data = {'username': 'Admin', 'password': 's3cr3tp4ssw0rd!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
