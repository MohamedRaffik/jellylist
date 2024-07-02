from django.test import TestCase, Client

from users.models import User


class TestGetUser(TestCase):
    def setUp(self):
        self.url = "/api/v1/users/session/"
        self.client = Client()
        self.user = User.objects.create_user(email="test", password="test")
        self.client.login(email=self.user.email, password="test")

    def test_get_user_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

    def test_get_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"email": self.user.email})


class TestCreateUser(TestCase):
    def setUp(self):
        self.url = "/api/v1/users/create/"
        self.client = Client()
        self.user = User.objects.create_superuser(email="test", password="test")
        self.client.login(email=self.user.email, password="test")

    def test_create_user_unauthenticated(self):
        self.client.logout()
        response = self.client.post(
            self.url,
            data={"email": "test2", "password": "test2"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 401)

    def test_create_user_as_not_superuser(self):
        self.client.logout()
        self.user.is_superuser = False
        self.user.save()
        self.client.login(email=self.user.email, password="test")
        response = self.client.post(
            self.url,
            data={"email": "test2", "password": "test2"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 401)

    def test_create_user(self):
        response = self.client.post(
            self.url,
            data={"email": "test2", "password": "test2"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200, response.content)
        self.assertEqual(response.json(), {"email": "test2"})
        self.assertTrue(User.objects.filter(email="test2").exists())


class TestLoginUser(TestCase):
    def setUp(self):
        self.url = "/api/v1/users/login/"
        self.client = Client()
        self.user = User.objects.create_user(email="test", password="test")

    def test_login_user_with_nonexistent_user(self):
        response = self.client.post(
            self.url,
            data={"email": "test2", "password": "test2"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 401)

    def test_login_user_with_wrong_password(self):
        response = self.client.post(
            self.url,
            data={"email": "test", "password": "test2"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 401)

    def test_login_user_with_wrong_email(self):
        response = self.client.post(
            self.url,
            data={"email": "test2", "password": "test"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 401)

    def test_login_user(self):
        response = self.client.post(
            self.url,
            data={"email": "test", "password": "test"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"email": "test"})
