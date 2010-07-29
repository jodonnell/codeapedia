from django.test import TestCase
from django.test.client import Client
from codea.models import HierarchyDB

class FrontPageTest(TestCase):
    fixtures = ['test.json']

    def setUp(self):
        self.client = Client()

    def test_front_page(self):
        response = self.client.get('/')

        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'Kent Beck')
