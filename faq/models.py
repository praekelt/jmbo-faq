from django.db import models

from jmbo.models import ModelBase

from ckeditor.fields import RichTextField


class FAQ(ModelBase):
    autosave_fields = ("question","answer",)

    question = models.TextField(
        help_text="A question frequently asked by users"
    )
    answer = RichTextField(
        help_text="An short but informative answer to the question"
    )

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
