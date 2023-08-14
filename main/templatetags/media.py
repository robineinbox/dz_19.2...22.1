# from django import template
# from django.conf import settings
#
# register = template.Library()
#
# @register.filter
# def media_url(value):
#     return f"{settings.MEDIA_URL}{value}"



from django import template
from django.conf import settings

register = template.Library()

@register.filter
def media_url(value):
    if value.startswith('/'):
        value = value[1:]
    return f"{settings.MEDIA_URL}{value}"