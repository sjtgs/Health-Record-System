from django.db import models

from insurance_app.models import Country, Province, Town, InusranceCompany


# Created Medical Information
class MedicalInformation(models.Model):
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    provinces = models.ForeignKey(Province, on_delete=models.CASCADE)
    towns = models.ForeignKey(Town, on_delete=models.CASCADE)
    hospital = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.hospital}"


class Diagnosis(models.Model):
    hospitals = models.ForeignKey(MedicalInformation, on_delete=models.CASCADE)
    diagnosis = models.TextField()

    def __str__(self):
        return f"{self.diagnosis}"


# Created Patient model. This model stores Patient Information
class Patient(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    # Basic Patient Information
    auto_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nrc = models.CharField(max_length=100)
    provinces = models.ForeignKey(Province, on_delete=models.CASCADE)
    towns = models.ForeignKey(Town, on_delete=models.CASCADE)
    address = models.TextField()

    # Medical information
    hospitals = models.ForeignKey(MedicalInformation, on_delete=models.CASCADE)
    medical_history = models.TextField()
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    treatment_plan = models.TextField()
    prescription = models.TextField()
    insurance = models.ForeignKey(InusranceCompany, on_delete=models.CASCADE)
    # Contact information
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Create Patient Image model to store the images for each patient
class PatientImage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="patient_images/")
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.patient.first_name} {self.patient.last_name}"
