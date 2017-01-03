from django.test import TestCase

from faq import models


class ModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(ModelTestCase, cls).setUpTestData()
        cls.faq = models.FAQ.objects.create(
            question="Does the model work?",
            answer="Yes, it does"
        )
            
    def test_faq_create(self):
        self.assertEquals(self.faq.question, "Does the model work?")
        self.assertEquals(self.faq.answer, "Yes, it does")

    def test_faq_update(self):
        faq = models.FAQ.objects.get(id=self.faq.id)
        faq.question = "Does it really work?"
        faq.answer = "Yes, no issues were identified"
        faq.save()
        self.assertEquals(self.faq.id, faq.id)
        self.assertEquals(faq.question, "Does it really work?")
        self.assertEquals(faq.answer, "Yes, no issues were identified")

    def test_faq_delete(self):
        self.faq.delete()
        exists = models.FAQ.objects.filter(id=self.faq.id).exists()
        self.assertFalse(exists)       
