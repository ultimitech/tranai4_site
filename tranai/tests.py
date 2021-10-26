from django.http import response
from django.test import TestCase

# Create your tests here.

class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_testregisterpage(self):
        response = self.client.get('/members/signup/')
        self.assertEqual(response.status_code, 200)

    def test_testloginpage(self):
        response = self.client.get('/members/login/')
        self.assertEqual(response.status_code, 200)