  
from django import template
from pages.models import BusinessInfo


register = template.Library()


@register.simple_tag(name="businessInfo")
def all_businessInfo():
    return BusinessInfo.objects.all()