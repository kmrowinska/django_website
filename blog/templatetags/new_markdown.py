from django import template
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()
@register.filter()
@stringfilter


def markdown(val):
    return md.markdown(val)