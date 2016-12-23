from django.conf.urls import patterns, include, url

from jmbo.views import ObjectDetail

urlpatterns = [
    url(
        r"^(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(
            template_name="faq/faq_detail.html"
        ),
        name="faq-categorized-detail"
    ),
    url(
        r"^(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(
            template_name="faq/faq_detail.html"
        ),
        name="faq-detail"
    ),
]
