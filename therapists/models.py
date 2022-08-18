from django.db import models

class Therapists(models.Model):
    id_document_n = models.IntegerField(primary_key=False, unique=True)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class TherapistDetails(models.Model):
    therapist = models.ForeignKey(
        Therapists,
        on_delete = models.CASCADE,
        related_name = 'therapist_details',
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
