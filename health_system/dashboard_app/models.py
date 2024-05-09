from django.db import models
from doctor_app.models import Doctor
from nurse_app.models import Nurse
from patient_app.models import Patient


class PatientReview(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    review_date = models.DateTimeField()
    purpose_review = models.TextField()

    def __str__(self):
        return f"{self.doctor.first_name}{self.doctor.last_name}{self.patient.first_name}{self.patient.last_name}"


# Review Appointment
class AppointmentReview(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    purpose = models.TextField()

    def __str__(self):
        return f"{self.doctor.first_name} {self.doctor.last_name} - {self.nurse.first_name} {self.nurse.last_name} - {self.patient.first_name} {self.patient.last_name}-{self.patient.patient_unit}"
