from rest_framework import serializers
from .models import Patients, PatientDetails, PatientSessions, Rooms, Shifts
from rest_framework.validators import UniqueValidator

class PatientsSerializer(serializers.ModelSerializer):
    patient_sessions = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    patient_details = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Patients
        fields = '__all__'

class PatientDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetails
        fields = '__all__'
        extra_kwargs= {
            'id_document_n': {
                'validators': [
                    UniqueValidator(
                        queryset = Patients.objects.all(),
                        message='This id document number already exists'
                    )
                ]
            }
        }

class PatientSessionsSerializer(serializers.ModelSerializer):
    session_bill = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = PatientSessions
        fields = '__all__'

class RoomsSerializer(serializers.ModelSerializer):
    room_shift = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    class Meta:
        model = Rooms
        fields = '__all__'

class ShiftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shifts
        fields = '__all__'