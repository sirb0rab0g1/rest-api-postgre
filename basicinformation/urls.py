from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import (
    InformationViewSet,
)


router = DefaultRouter()
router.register(r'personal', InformationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
