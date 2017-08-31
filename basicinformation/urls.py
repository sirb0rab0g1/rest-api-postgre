from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .models import Information
from .views import (
    InformationViewSet,
)

router = DefaultRouter()


urlpatterns = [
    
    url(r'^', include(router.urls)),

]
