  
from django import template
from pages.models import BusinessInfo
from cars.models import Car


register = template.Library()


@register.simple_tag(name="businessInfo")
def all_businessInfo():
    return BusinessInfo.objects.all()


@register.simple_tag(name="cars")
def all_cars():
    return Car.objects.all()