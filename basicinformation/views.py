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
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
    
    @detail_route(methods=['GET'])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.first_name)

# class InformationListView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         queryset = Information.objects.all()
#         serializer_class = InformationSerializer(queryset, many=True)
#         return Response(serializer_class.data)

#     def post(self, request, format=None):
#         serializer_class = InformationSerializer(data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return Response(serializer_class.data, status=status.HTTP_201_CREATED)
#         return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

# class InformationListRequest(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Information.objects.get(pk=pk)
#         except Information.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = InformationSerializer(snippet)
#         return Response(serializer.data)
        
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = InformationSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
