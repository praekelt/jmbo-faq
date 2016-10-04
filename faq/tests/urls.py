from django.conf.urls import include, url


urlpatterns = [
    url(r"^jmbo/", include("jmbo.urls"))
]
