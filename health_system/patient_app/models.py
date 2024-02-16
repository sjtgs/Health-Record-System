from django.contrib.auth.models import User
from django.db import models
from insurance_app.models import Country, Province, Town, InsuranceCompany


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    BLOOD_CHOICES = [("A", "BLOOD A"), ("B", "BLOOD B"), ("O", "BLOOD O")]
    UNIT_CHOICES = [("U1", "UNIT 1"), ("U2", "UNIT 2"), ("U3", "UNIT 3")]
    PATIENT_TYPE_CHOICES = [("OP", "OUTWARD PATIENT"), ("IP", "INWARD PATIENT")]

    # Basic Patient Information
    auto_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nrc = models.CharField(max_length=100)
    patient_type = models.CharField(max_length=3, choices=PATIENT_TYPE_CHOICES)
    provinces = models.ForeignKey(Province, on_delete=models.CASCADE)
    towns = models.ForeignKey(Town, on_delete=models.CASCADE)
    address = models.TextField()

    # Medical information
    hospitals = models.ForeignKey(MedicalInformation, on_delete=models.CASCADE)
    medical_history = models.TextField()
    blood_type = models.CharField(max_length=1, choices=BLOOD_CHOICES)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    patient_unit = models.CharField(max_length=3, choices=UNIT_CHOICES)
    treatment_plan = models.TextField()
    prescription = models.TextField()
    insurance = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    # Contact information

    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        # Check if the user doesn't exist, create a new one. The username and the password same
        if not self.user:
            username = (self.first_name[:2] + self.last_name[:2] + self.nrc[:4]).lower()
            password = username
            self.user = User.objects.create_user(username=username, password=password)

        super().save(*args, **kwargs)


# Create Patient Image model to store the images for each patient
class PatientImage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="patient_images/")
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.patient.first_name} {self.patient.last_name}"
