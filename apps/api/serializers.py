from rest_framework.serializers import *

from apps.client.models import Client

class ClientSerializer(ModelSerializer):

    class Meta:

        model = Client
        fields = '__all__'