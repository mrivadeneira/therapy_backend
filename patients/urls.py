from django.urls import path
from . import views

urlpatterns = [
    path('patients/',views.PatientsView.as_view()),
    path('patients-admin/',views.PatientsAdminView.as_view()),
    path('patients/<int:pk>',views.PatientChangeView.as_view()),
    path('patient_sessions/',views.SessionsView.as_view()),
    path('patient_sessions/<int:pk>',views.PatientSessionsChangeView.as_view()),
    path('patient_details/',views.PatientDetailsView.as_view()),
    path('patient_details/<int:pk>',views.PatientDetailsChangeView.as_view()),
    path('rooms/',views.RoomsView.as_view()),
    path('rooms/<int:pk>',views.RoomChangeView.as_view()),
    path('shifts/',views.ShiftsView.as_view()),
    path('shifts/<int:pk>',views.ShiftChangeView.as_view()),
]
