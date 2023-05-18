from django.contrib.auth.models import User as UserDjango
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.user_api.models import User


class UserTestCase(TestCase):
    def setUp(self):
        self.user_django = UserDjango.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.user = User.objects.create(
            name="John Doe",
            cpf="12345678901",
            email="johndoe@example.com",
            phone_number="1234567890",
        )
        self.user2 = User.objects.create(
            name="John 2",
            cpf="987654321",
            email="johndoe2@example.com",
            phone_number="1234567890",
        )
        self.user3 = User.objects.create(
            name="John 3",
            cpf="1234234234",
            email="johndoe3@example.com",
            phone_number="1234567890",
        )
        self.client = APIClient()
        self.client_not_authorization = APIClient()
        self.client.force_authenticate(user=self.user_django)

    def test_user_list(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 3)

    def test_create_user(self):
        new_user_data = {
            "name": "Jane Smith",
            "cpf": "1234567890",
            "email": "jane.smith@example.com",
            "phone_number": "9876543210",
        }
        url = reverse("user-list")
        response = self.client.post(url, data=new_user_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 4)

        created_user = User.objects.get(cpf=new_user_data["cpf"])

        self.assertEqual(created_user.name, new_user_data["name"])
        self.assertEqual(created_user.email, new_user_data["email"])
        self.assertEqual(
            created_user.phone_number,
            new_user_data["phone_number"]
            )

        response_data = response.json()
        self.assertEqual(response_data["name"], new_user_data["name"])
        self.assertEqual(response_data["email"], new_user_data["email"])
        self.assertEqual(
            response_data["phone_number"], new_user_data["phone_number"])

    def test_retrieve_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data["id"], self.user.id)
        self.assertEqual(response_data["name"], self.user.name)
        self.assertEqual(response_data["cpf"], self.user.cpf)
        self.assertEqual(response_data["email"], self.user.email)
        self.assertEqual(response_data["phone_number"], self.user.phone_number)

    def test_update_user(self):
        url = reverse("user-detail", args=[self.user.id])

        valid_data = {
            "name": "John Updated",
            "cpf": "98765432100",
            "email": "john.updated@example.com",
            "phone_number": "1234567890",
        }

        response = self.client.patch(url, data=valid_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_user_with_invalid_data(self):
        invalid_data = {
            "name": "",
            "cpf": "123",
            "email": "john.doe@example",
            "phone_number": "987654321",
        }

        url = reverse("user-list")
        response = self.client.post(url, data=invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {
                "name": ["This field may not be blank."],
                "cpf": ["(123) is not valid cpf."],
                "email": ["Enter a valid email address."],
            },
        )

    def test_retrieve_nonexistent_user(self):
        url = reverse("user-detail", args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_user_with_invalid_data(self):
        url = reverse("user-detail", args=[self.user.id])

        invalid_data = {
            "cpf": "123",
            "email": "john.doe@example",
            "phone_number": "987654321",
        }

        response = self.client.patch(url, data=invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {
                "cpf": ["(123) is not valid cpf."],
                "email": ["Enter a valid email address."],
            },
        )

    def test_delete_nonexistent_user(self):
        url = reverse("user-detail", args=[9999])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_without_authorization(self):
        url = reverse("user-detail", args=[9999])
        response = self.client_not_authorization.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_without_authorization(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client_not_authorization.patch(url, data={})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_without_authorization(self):
        url = reverse("user-detail", args=[9999])
        response = self.client_not_authorization.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user_without_authorization(self):
        url = reverse("user-list")
        response = self.client_not_authorization.post(url, data={})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_filter_users_by_cpf(self):
        url = reverse("user-list")
        response = self.client.get(f"{url}?cpf=123")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)
        self.assertEqual(response.data["results"][0]["name"], "John Doe")
        self.assertEqual(response.data["results"][1]["name"], "John 3")

    def test_filter_users_by_nonexistent_cpf(self):
        url = reverse("user-list")
        response = self.client.get(f"{url}?cpf=999.")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 0)
