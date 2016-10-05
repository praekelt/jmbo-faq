from django.contrib import admin

from jmbo.admin import ModelBaseAdmin

from faq.models import FAQ


admin.site.register(FAQ, ModelBaseAdmin)
