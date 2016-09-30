from django.test import TestCase

from faq import models


def load_fixtures(kls):
    kls.FAQ = models.FAQ.objects.create(
        question = "Does the model work?",
        answer = "Yes, it does"

    )

class ModelTestCase(TestCase):

    @classmethod
    def setUpClass(self):
        load_fixtures(self)
            
    def test_faq_create(self):
        # Ensure model was saved correctly
        self.assertEquals(self.FAQ.question, "Does the model work?")
        self.assertEquals(self.FAQ.answer, "Yes, it does")

    def test_faq_update(self):
        # Ensure model is updated
        faq = models.FAQ.objects.get(id=self.FAQ.id)
        faq.question = "Does it really work?"
        faq.answer = "Yes, no issues were identified"
        faq.save()
        self.assertEquals(self.FAQ.id, faq.id)
        self.assertEquals(faq.question, "Does it really work?")
        self.assertEquals(faq.answer, "Yes, no issues were identified")

    def test_faq_delete(self):
        # Ensure model is deleted
        self.FAQ.delete()
        exists = models.FAQ.objects.filter(id=self.FAQ.id).exists()
        self.assertFalse(exists)       

    @classmethod
    def tearDownClass(self):
        del self.FAQ
