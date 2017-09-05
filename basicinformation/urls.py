from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

from .models import Information
from .views import (
    InformationViewSet,
    
    information_list,
    information_request
)
router = DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^information-list/$', information_list.as_view()),
    url(r'^information-request/(?P<pk>[0-9]+)/$', information_request.as_view()),
]


