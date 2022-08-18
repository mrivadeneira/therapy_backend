from .models import Therapists, TherapistDetails
from .serializers import TherapistsSerializer, TherapistDeatilsSerializer
from rest_framework import generics

class TherapistsAPIView(generics.ListCreateAPIView):
    queryset = Therapists.objects.all()
    serializer_class = TherapistsSerializer

class TherapistChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Therapists.objects.all()
    serializer_class = TherapistsSerializer

class TherapistDetailsAPIView(generics.ListCreateAPIView):
    queryset = TherapistDetails.objects.all()
    serializer_class = TherapistDeatilsSerializer

class TherapistDetailsChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TherapistDetails.objects.all()
    serializer_class = TherapistDeatilsSerializer
