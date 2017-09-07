from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

from .models import Information
from .views import (
    InformationViewSet,
)


router = DefaultRouter()

information_list = InformationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
information_request = InformationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^personal/$', information_list, name='information_list'),
    url(r'^personal/(?P<pk>[0-9]+)/$', information_request, name='information_request'),
]


