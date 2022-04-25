from django.test import TestCase
import json
from django.urls import reverse, resolve



class UrlsTests(TestCase):
    def test_fibonacci(self):
        url = reverse('fibonacci')
        response = self.client.post(url, data={
                    'n': 3
                }, format=json)
        self.assertEqual(response.status_code, 200)

    def test_ackermann(self):
        url = reverse('ackermann')
        response = self.client.post(url, data={
            'n': 3,
            'm': 0
        }, format=json)
        self.assertEquals(response.status_code, 200)

    def test_factorial(self):
        url = reverse('factorial')
        response = self.client.post(url, data={
            'n': 3
        }, format=json)
        self.assertEquals(response.status_code, 200)

