from django import template
from mainapp.models import *

register = template.Library()

def range_filter(value):
    return value[0:200] + "...."

register.filter('range_filter',range_filter)

def range_filter_long(value):
    return value[0:300] + "<strong>...<a href="">see more</a></strong>"

register.filter('range_filter_long',range_filter_long)


@register.filter
def companyprofile(request):
    return Companyprofile.objects.all().last()
register.filter('companyprofile',companyprofile)
