from rest_framework.status import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)

from .serializers import ClientSerializer
from apps.client.models import Client

class ClientViewSet(ViewSet):

    # authentication_classes = (SessionAuthentication, TokenAuthentication)

    def list(self, request):

        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(
            data=serializer.data,
            status=HTTP_200_OK
        )
    
    def create(self, request):

        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )
    
    def destroy(self, request, pk=None):

        client = Client.objects.get(pk=pk)
        client.delete()
        return Response(
            'Deleted',
            status=HTTP_204_NO_CONTENT
        )