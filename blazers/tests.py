from django.test import TestCase


# Create your tests here.

class URLtests(TestCase):
    def test_testhome(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)

class URLtests(TestCase):
    def test_testBlazers(self):
        response = self.client.get('blazers')
        self.assertEqual(response.status_code,300)


