from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from insurance_app.models import Country, Province, Town
from patient_app.models import MedicalInformation


# Created Doctor model to store Doctor Information
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    # Basic Doctor Information
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
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        # Check if the user doesn't exist, Create new one.The username and the password same
        if not self.user:
            username = (self.first_name[:2] + self.last_name[:2] + self.nrc[:4]).lower()
            password = username
            self.user = User.objects.create_user(username=username, password=password)

        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def assign_doctor_group(sender, instance, created, **kwargs):
    if created and hasattr(instance, "doctor"):
        doctor_group = Group.objects.get(name="Doctor")
        instance.groups.add(doctor_group)


class DoctorImage(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="medical_stuff_images/doctor_images/")
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.doctor.first_name} {self.doctor.last_name}"
