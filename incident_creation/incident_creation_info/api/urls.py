from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from incident_creation_info.api import views
from django.conf.urls.static import static
from .views import (
    IncidentCreationInfoViewSet,
)

router = DefaultRouter()
router.register('incidents', IncidentCreationInfoViewSet, basename='incident')
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)