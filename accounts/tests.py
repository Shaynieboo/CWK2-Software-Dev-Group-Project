from django.test import TestCase
from django.contrib.auth.models import User

class UsersTestLogin(TestCase):
    def test_login_user(self):
        # Create user
        self.user = User.objects.create_user(username="test", password="123")

        # Log in the user
        login = self.client.login(username="test", password="123")

        # Check if login was successful
        self.assertTrue(login)
