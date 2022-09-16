from django import template
from mainapp.models import *

register = template.Library()

@register.filter
def service(request):
    return Ourserver.objects.all()

@register.filter
def project(request):
    return Ourproject.objects.all()