import unittest

from django.test.client import Client

from faq.models import FAQ


class ViewsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = Client()

        obj, created = FAQ.objects.get_or_create(
            question="Is this a test?",
            answer="Yes, it is"
        )
        cls.faq = obj

    def test_faq(self):
        pass

    @ classmethod
    def tearDownClass(cls):
        del cls.client
        del cls.faq
