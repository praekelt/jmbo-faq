from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^jmbo/", include("jmbo.urls")),
    url(r"^faq/", include("faq.urls"))
]
