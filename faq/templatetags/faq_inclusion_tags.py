from django import template

register = template.Library()


@register.inclusion_tag("faq/inclusion_tags/faq_detail.html")
def faq_detail(obj):
    return {"object": obj}
