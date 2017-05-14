from django.conf.urls import url

from jmbo.views import ObjectDetail

urlpatterns = [
    url(
        r"^(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(),
        name="faq-categorized-detail"
    ),
    url(
        r"^(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(),
        name="faq-detail"
    ),
]
