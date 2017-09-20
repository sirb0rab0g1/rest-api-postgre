import base64

from basicinformation.serializers import InformationSerializer
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from .models import (
    Information
)

from rest_framework.decorators import (
    api_view,
    detail_route,
)
from rest_framework.response import Response
from rest_framework import (
    viewsets,
)


@api_view(['POST'])
def upload_profile_image(request):
    image_uri = request.data['img_uri']
    profile_id = request.data['id']
    file_name = request.data['image']

    account = get_object_or_404(Information, id=profile_id)
    imgstr = image_uri.split(';base64,')[1]
    account.image.save(file_name, ContentFile(base64.b64decode(imgstr)))

    return Response({'image': account.image.url})


class InformationViewSet(viewsets.ModelViewSet):
    """s
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Information.objects.all()
    serializer_class = InformationSerializer

    @detail_route(methods=['GET'])
    def get_details(self, request, pk=None):
        snippet = self.get_object()
        data = {
            'id': snippet.id,
            'first_name': snippet.first_name,
            'middle_name': snippet.middle_name,
            'last_name': snippet.last_name,
            'age': snippet.age,
            'email': snippet.email,
            'image': snippet.image
        }
        return Response(data)
