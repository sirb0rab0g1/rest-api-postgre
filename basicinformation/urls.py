from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .models import Information
from .views import (
    InformationViewSet,
    delete_user
)

router = DefaultRouter()
router.register(r'info', InformationViewSet)

urlpatterns = [
    
    url(r'^', include(router.urls)),
    url(r'^delete-user$', delete_user, name='delete_user'),
]

