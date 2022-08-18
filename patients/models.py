from django.db import models
from security.models import UserAccount

class Patients(models.Model):
    id_document_n = models.IntegerField(primary_key=False, unique=True) #Unique field validated in serializers.py
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        UserAccount,
        on_delete = models.SET("DELETED"),
        related_name="created_by_patient",
        null=True
        )
    updated_by = models.ForeignKey(
        UserAccount,
        on_delete = models.SET("DELETED"),
        related_name='updated_by_patient',
        null=True,
    )
    updated_at = models.DateTimeField(null=True)

    
class PatientDetails(models.Model):
    patient = models.ForeignKey(
        Patients,
        on_delete = models.CASCADE,
        related_name = 'patient_details',
    )
    email = models.EmailField(max_length=254)
    mobile_1 = models.PositiveBigIntegerField()
    mobile_2 = models.PositiveBigIntegerField(null=True)
    zip_code = models.SmallIntegerField()
    address_street = models.CharField(max_length=200)
    address_num = models.IntegerField()
    address_floor = models.CharField(max_length=10, null=True)
    address_ap = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PatientSessions(models.Model):
    patient = models.ForeignKey(
        Patients,
        on_delete = models.CASCADE,
        related_name = 'patient_sessions',
    )
    therapist = models.ForeignKey(
        'therapists.Therapists',
        on_delete = models.SET('DELETED'),
        related_name = 'therapist_session'
    )
    date = models.DateField()
    time = models.TimeField()
    class Guardian(models.IntegerChoices):
        NO = 1
        YES = 2
    guardian = models.IntegerField(choices=Guardian.choices)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Rooms(models.Model):
    door = models.CharField(max_length=50)

class Shifts(models.Model):
    is_recurrent = models.BooleanField(default=False)
    day_start = models.DateField()
    day_end = models.DateField(null=True)
    time_start = models.TimeField()
    time_end = models.TimeField()
    room = models.ForeignKey(
        Rooms,
        on_delete = models.CASCADE,
        related_name = 'room_shift'
    )
    therapist = models.ForeignKey(
        'therapists.Therapists',
        on_delete = models.CASCADE,
        related_name = 'therapist_shift',
    )
    class Meta:
        unique_together = ('room','day_start','time_start')