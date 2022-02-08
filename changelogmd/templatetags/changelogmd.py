import markdown

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def markdownify(text):
    html = markdown.markdown(text or "")
    return mark_safe(html)
