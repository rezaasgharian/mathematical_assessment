import json
from django.test import TestCase
from django.urls import reverse


# # Create your tests here.
class ViewsTests(TestCase):
    def testFibonacci(self):
        url = reverse('fibonacci')
        response = self.client.post(url, data={
            'n': 3
        }, format=json)
        self.assertEqual(json.loads(response.content), {
            'result':2
        })

    def testAckermann(self):
        url = reverse('ackermann')
        response = self.client.post(url, data={
            'm': 0,
            'n': 3,
        }, format=json)
        self.assertEqual(json.loads(response.content), {
            'result':4
        })

    def testFactorial(self):
        url = reverse('factorial')
        response = self.client.post(url, data={
            'n':3
        }, format=json)
        self.assertEqual(json.loads(response.content), {
            'result': 6
        })


