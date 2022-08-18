from .models import Patients, PatientDetails, PatientSessions, Rooms, Shifts
from .serializers import PatientsSerializer, PatientDetailsSerializer, PatientSessionsSerializer, RoomsSerializer, ShiftsSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from security.checks import IsAdminCheck
from django.utils import timezone

class PatientsView(generics.ListCreateAPIView):
    serializer_class = PatientsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['lastname']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patients.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PatientsAdminView(IsAdminCheck,generics.ListCreateAPIView):
    serializer_class = PatientsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['lastname']

    def get_queryset(self):
        return Patients.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PatientChangeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def perform_update(self,serializer):
        serializer.save(
            updated_by=self.request.user,
            updated_at=timezone.now()
        )


class SessionsView(generics.ListCreateAPIView):
    queryset = PatientSessions.objects.all()
    serializer_class = PatientSessionsSerializer

class PatientSessionsChangeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientSessions.objects.all()
    serializer_class = PatientSessionsSerializer

class PatientDetailsView(generics.ListCreateAPIView):
    class DetailsFilter(FilterSet):
        class Meta:
            model = PatientDetails
            fields = '__all__'
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer
    filter_class = DetailsFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,]
    search_fields = ['=id_document_n', '$email',]
    ordering_fields = ('patient',)

class PatientDetailsChangeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer

class RoomsView(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class RoomChangeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class ShiftsView(generics.ListCreateAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftsSerializer

class ShiftChangeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shifts.objects.all()
    serializer_class = ShiftsSerializer