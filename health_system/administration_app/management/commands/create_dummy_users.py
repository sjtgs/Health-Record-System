# Create Dummy Users - Administrator , Doctor , Nurse and Patient

from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand
from administration_app.models import Administrator
from doctor_app.models import Doctor
from nurse_app.models import Nurse
from patient_app.models import Patient


class Command(BaseCommand):
    help = "Create Dummy data for Administrator , Doctor, Nurse, Patient users"

    def handle(self, *args, **options):

        # Create Administrator Users - 5
        administrator_group, _ = Group.objects.get_or_create(name="Administrator")
        for i in range(5):
            administrator = User.objects.create(
                username=f"admin{i}", is_staff=True, is_superuser=True
            )
            administrator.groups.add(administrator_group)
            Administrator.objects.create(user=administrator)
            self.stdout.write(
                self.style.SUCCESS(f"Administrator created: {administrator.username}")
            )

        # Create Doctor Users - 15
        doctor_group, _ = Group.objects.get_or_create(name="Doctor")
        for i in range(15):
            doctor = User.objects.create(username=f"doctor{i}")
            doctor.groups.add(doctor_group)
            Doctor.objects.create(user=doctor)
            self.stdout.write(self.style.SUCCESS(f"Doctor created: {doctor.username}"))

        # Create Nurse Users - 20
        nurse_group, _ = Group.objects.get_or_create(username="Nurse")
        for i in range(20):
            nurse = User.objects.get_or_create(username=f"nurse{i}")
            nurse.groups.add(nurse_group)
            Nurse.objects.create(user=nurse)
            self.stdout.write(self.style.SUCCESS(f"Nurse created: {nurse.username}"))

        # Create Patient Users - 50
        patient_group, _ = Group.objects.get_or_create(name="Patient")
        for i in range(50):
            patient = User.objects.create(username=f"Patient{i}")
            patient.groups.add(patient_group)
            Patient.objects.create(user=patient)
            self.stdout.write(
                self.style.SUCCESS(f"Patient created: {patient.username}")
            )
