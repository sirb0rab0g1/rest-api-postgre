from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from basicinformation.serializers import InformationSerializer


from rest_framework.decorators import (
    api_view,
    detail_route,
    permission_classes,
)

from .models import (
    Information
)
from .serializers import (
    InformationSerializer,
)

from rest_framework import (
    permissions,
    status,
    viewsets,
)
        
class InformationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

@api_view(['POST'])
def delete_user(request):
    user = User.objects.get(id=request.data['id'])
    return Response({'success': True}, status=status.HTTP_200_OK)