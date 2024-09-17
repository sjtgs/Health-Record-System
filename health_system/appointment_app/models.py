from django.db import models

from doctor_app.models import Doctor
from patient_app.models import Patient


# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"The Appointment for {self.patient.first_name} {self.patient.last_name} {self.patient.date_of_birth} {self.patient.nrc} with Doctor {self.doctor.first_name} {self.doctor.last_name} on  {self.date} time {self.time} "
