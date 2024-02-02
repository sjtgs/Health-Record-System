from django.db import models
from doctor_app.models import Doctor
from patient_app.models import Patient


class PatientReview(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    review_date = models.DateTimeField()
    purpose_review = models.TextField()

    def __str__(self):
        return f"{self.doctor.first_name}{self.doctor.last_name}{self.patient.first_name}{self.patient.last_name}"
