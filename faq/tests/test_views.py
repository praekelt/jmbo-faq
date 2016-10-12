import unittest

from django.test.client import Client

from faq.models import FAQ


class ViewsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = Client()

        obj, created = FAQ.objects.get_or_create(
            title="faq",
            question="Is this a test?",
            answer="Yes, it is",
            state="Published"
        )
        obj.sites = [1]
        cls.faq = obj

    def test_pagination(self):
        response = self.client.get(self.faq.get_absolute_url())

    @classmethod
    def tearDownClass(cls):
        del cls.client
        del cls.faq
