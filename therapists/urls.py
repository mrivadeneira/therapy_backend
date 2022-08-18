from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('therapists/', views.TherapistsAPIView.as_view()),
    path('therapists/<int:pk>', views.TherapistChangeAPIView.as_view()),
    path('therapist_details/', views.TherapistDetailsAPIView.as_view()),
    path('therapist_details/<int:pk>', views.TherapistDetailsChangeAPIView.as_view()),
]
