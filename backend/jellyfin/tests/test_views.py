from django.test import TestCase, Client

from jellyfin.models import JellyfinServer
from users.models import User


class TestGetServer(TestCase):
    def setUp(self):
        self.url = "/api/v1/jellyfin/server/"
        self.client = Client()
        self.user = User.objects.create_user(email="test", password="test")
        self.client.login(email=self.user.email, password="test")

    def test_get_server_when_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

    def test_get_server_when_user_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "No Jellyfin server configured"})

    def test_get_server_when_server_configured(self):
        server = JellyfinServer.objects.create(name="test", url="http://test.com")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"name": server.name, "url": server.url})
