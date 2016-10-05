from jmbo import api as jmbo_api

from faq.models import FAQ

import rest_framework_extras


class FAQObjectsViewSet(jmbo_api.ModelBaseObjectsViewSet):
    queryset = FAQ.objects.all()


class FAQPermittedViewSet(jmbo_api.ModelBasePermittedViewSet):
    queryset = FAQ.permitted.all()


def register(router):
    return rest_framework_extras.register(
        router,
        (
            ("faq-faq-permitted", FAQPermittedViewSet),
            ("faq-faq", FAQObjectsViewSet)
        )
    )
