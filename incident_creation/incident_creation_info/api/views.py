from rest_framework.views import APIView
from .serializers import IncidentCreationInfoSerializers
from rest_framework.viewsets import ModelViewSet
from incident_creation_info.models import IncidentCreationInfo


class IncidentCreationInfoViewSet(ModelViewSet):
    queryset = IncidentCreationInfo.objects.all()
    serializer_class = IncidentCreationInfoSerializers

