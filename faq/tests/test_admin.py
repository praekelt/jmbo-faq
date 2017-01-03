from django.contrib.auth import get_user_model
from django.test import TestCase

from jmbo.models import Relation

from faq.models import FAQ


class AdminTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(AdminTestCase, cls).setUpTestData()
        cls.testuser = get_user_model().objects.create(
            username="testuser",
            email="testemail@test.com",
            is_superuser=True,
            is_staff=True
        )
        cls.testuser.set_password("password")
        cls.testuser.save()

        obj, created = FAQ.objects.get_or_create(
            question="Does this exist?",
            answer="Yes, it does."
        )
        obj.save()
        cls.faq = obj

        Relation.objects.create(
            source_content_type=cls.faq.content_type,
            source_object_id=0,
            target_content_type=cls.faq.content_type,
            target_object_id=0,
            name="faq_faqs"
        )

    def setUp(self):
        super(AdminTestCase, self).setUp()
        self.client.login(username="testuser", password="password")

    def test_admin_add(self):
        response = self.client.get("/admin/faq/faq/add/")
        self.assertEquals(response.status_code, 200)

    def test_admin_change(self):
        response = self.client.get("/admin/faq/faq/%s/change/" % self.faq.pk)
        self.assertEquals(response.status_code, 200)

    def test_admin_relation(self):
        response = self.client.get("/admin/faq/faq/add/")
        self.failUnless("Faq faqs" in response.content)