from django.db import models
from insurance_app.models import Country, Province, Town
from patient_app.models import MedicalInformation


#  Nurse Model to store Information
class Nurse(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    # Basic Nurse Information
    auto_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nrc = models.CharField(max_length=100)
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    provinces = models.ForeignKey(Province, on_delete=models.CASCADE)
    towns = models.ForeignKey(Town, on_delete=models.CASCADE)
    address = models.TextField()

    # Medical Information
    medical_number = models.PositiveIntegerField()
    hospitals = models.ForeignKey(MedicalInformation, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    years_of_experience = models.PositiveIntegerField()

    # Contact Information
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class NurseImage(models.Model):
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="medical_stuff_images/nurse_images/")
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.doctor.first_name} {self.doctor.last_name}"