from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import (
    upload_profile_image,
    InformationViewSet,
)

router = DefaultRouter()
router.register(r'personal', InformationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^upload-profile-image/$', upload_profile_image, name='upload_profile_image'),
]
