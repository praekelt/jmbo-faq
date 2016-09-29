from django.conf.urls import include, url


urlpatterns = [
    url(r"ˆfaq/", include("faq.urls")),
]
