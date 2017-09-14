from basicinformation.serializers import InformationSerializer


from rest_framework.decorators import (
    detail_route,
)

from rest_framework.response import Response

from .models import (
    Information
)

from rest_framework import (
    viewsets,
)


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
            'email': snippet.email
        }
        return Response(data)
