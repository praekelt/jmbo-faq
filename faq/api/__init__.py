from jmbo import api as jmbo_api

from faq.models import FAQ


class FAQObjectsViewSet(jmbo_api.ModelBaseObjectsViewSet):
    queryset = FAQ.objects.all()


class FAQPermittedViewSet(jmbo_api.ModelBasePermittedViewSet):
    queryset = FAQ.permitted.all()


def register(router):
    router.register(
        r"faq-faq",
        FAQObjectsViewSet
    )
    router.register(
        r"faq-faq-permitted",
        FAQPermittedViewSet
    )
