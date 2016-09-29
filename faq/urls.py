from django.conf.urls import patterns, include, url

from jmbo.views import ObjectDetail

urlpatterns = [
    url(
        r"^(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(),
        name="faq-faq-detail"
    ),
]
