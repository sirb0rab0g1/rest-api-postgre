from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from basicinformation.serializers import InformationSerializer
from rest_framework.permissions import AllowAny


from rest_framework.decorators import (
    api_view,
    detail_route,
    permission_classes,
)

from rest_framework.response import Response

from .models import (
    Information
)
from .serializers import (
    InformationSerializer,
)

from rest_framework import (
    permissions,
    viewsets,
)

from rest_framework import renderers
        
class InformationViewSet(viewsets.ModelViewSet):
    """s
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
    
    @detail_route(methods=['GET'])
    def get_details(self, request, pk=None):
        snippet = self.get_object()
        data = {
            'id':snippet.id,
            'first_name':snippet.first_name,
            'middle_name':snippet.middle_name,
            'last_name':snippet.last_name
        }
        return Response(data)
    
    