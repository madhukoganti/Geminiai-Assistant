
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class ChatValidationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_empty_message(self):
        response = self.client.post(
            '/chatbot/chat/',
            {'message': ''},
            format='json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data['error'],
            'Message cannot be empty.'
        )

    def test_whitespace_message(self):
        response = self.client.post(
            '/chatbot/chat/',
            {'message': '     '},
            format='json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data['error'],
            'Message cannot be empty.'
        )

    # ADD THE NEW TEST HERE 👇
    def test_non_string_message(self):
        response = self.client.post(
            '/chatbot/chat/',
            {'message': 123},
            format='json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data['error'],
            'Message must be text.'
        )
    def test_message_too_long(self):
        long_message = 'a' * 5001

        response = self.client.post(
            '/chatbot/chat/',
            {'message': long_message},
            format='json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data['error'],
            'Message is too long. Please keep it under 5000 characters.'
        )    