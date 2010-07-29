from django.test import TestCase
from django.test.client import Client
from codea.models import HierarchyDB

BROKEN_WINDOWS = 'broken windows'

class FrontPageTest(TestCase):
    fixtures = ['test.json']

    def setUp(self):
        self.client = Client()

    def test_front_page(self):
        response = self.client.get('/')

        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'Kent Beck')
        self.assertContains(response, 'Implementation Patterns')
        self.assertContains(response, 'Fan out')

    def test_by_author(self):
        response = self.client.get('/by_author', {'id':2})
        self.assertContains(response, BROKEN_WINDOWS)

    def test_by_tag(self):
        response = self.client.get('/by_tag', {'id':1})
        self.assertContains(response, BROKEN_WINDOWS)

    def test_by_book(self):
        response = self.client.get('/by_book', {'id':7})
        self.assertContains(response, BROKEN_WINDOWS)
