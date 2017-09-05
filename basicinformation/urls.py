from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

from .models import Information
from .views import (
    InformationViewSet,
    InformationListView,
    InformationListRequest
)

router = DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^information-list/$', InformationListView.as_view()),
    url(r'^information-request/(?P<pk>[0-9]+)/$', InformationListRequest.as_view()),
]


