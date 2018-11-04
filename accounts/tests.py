from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from django.contrib.auth import login, logout

from users.models import CustomUser
# Create your tests here.
class TestAuthentication(TestCase):
    def test_sign_in_9(self):

        user = CustomUser.objects.create(username='testuser', email='tester@email.com')
        user.set_password('12345')
        user.save()
        client = Client()
        logged_in = client.login(username='testuser', password='12345')
        self.assertTrue(login)
        self.assertTrue(user.is_authenticated)

    def test_sign_out_10(self):

        user = CustomUser.objects.create(username='testuser', email='tester@email.com')
        user.set_password('12345')
        user.save()

        client = Client()
        logged_in = client.login(username='testuser', password='12345')
        client.logout
        self.assertTrue(logout)
