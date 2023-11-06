from django.contrib.admin import *

from .models import Client

@register(Client)
class ClientAdmin(ModelAdmin):

    list_display = ('id', 'fullname', 'date_of_birth')
    list_display_links = ('id', 'fullname', 'date_of_birth')