from rest_framework import serializers

from incident_creation_info.models import IncidentCreationInfo

class IncidentCreationInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = IncidentCreationInfo
        fields = '__all__'



