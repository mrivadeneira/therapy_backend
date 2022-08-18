from rest_framework import serializers
from .models import Therapists, TherapistDetails

class TherapistsSerializer(serializers.ModelSerializer):
    therapist_session = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    therapist_shift = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Therapists
        fields = '__all__'

class TherapistDeatilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapistDetails
        fields = '__all__'