from unicodedata import category
from django import template
from ipware import get_client_ip

from voting.models import Vote
register = template.Library()


@register.filter
def has_voted(category, request):

    ipaddress= get_client_ip(request)

    if(Vote.objects.filter(category=category, ipaddress=ipaddress).exists()):
        return True
    else:
        return False
