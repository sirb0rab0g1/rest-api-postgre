from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

from .models import Information
from .views import (
    InformationViewSet,
)


router = DefaultRouter()
router.register(r'personal', InformationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]


