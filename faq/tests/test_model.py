from django.test import TestCase

from faq import models

class ModelTestCase(TestCase):
    def setUp(self):
        self.FAQ = models.FAQ(
            question = "Does the model work?",
            answer = "Yes, it does"
        )

    def test_faq_model(self):
        # Ensure model was saved correctly
        self.assertEquals(self.FAQ.question, "Does the model work?")
        self.assertEquals(self.FAQ.answer, "Yes, it does")

        # Ensure model is updated
        self.FAQ.question = "Does it really work?"
        self.FAQ.answer = "Yes, no issues were identified"
        self.FAQ.save()
        self.assertEquals(self.FAQ.question, "Does it really work?")
        self.assertEquals(self.FAQ.answer, "Yes, no issues were identified")

    def tearDown(self):
        del self.FAQ
