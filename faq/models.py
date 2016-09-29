from django.db import models

from jmbo.models import ModelBase


class FAQ(ModelBase):
    autosave_fields = ("question","answer",)

    question = models.TextField(
        blank=True,
        null=True,
    )

    answer = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
