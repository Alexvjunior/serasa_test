from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name='John Doe', cpf='12345678901', email='johndoe@example.com', phone_number='1234567890')

    def test_user_list(self):
        url = reverse('api/user-list')
        response = self.client.get(url)
        assert self.assertEqual(response.status_code, 200)
        assert self.assertEqual(len(response.json()), 1)
        assert 1 == 0