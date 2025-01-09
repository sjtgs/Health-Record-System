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
    

# Patient Information Appointment 
class PatientMedicalInfo(models.Model):
    patient =  models.ForeignKey(Patient, on_delete=models.CASCADE)
    weight = models.IntegerField()
    height = models.IntegerField()
    blood_pressure = models.IntegerField()
    

    def __str__(self):
        return f"Patient Medical Information {self.patient.first_name} {self.patient.last_name} "

# Medical Notes from the Doctor and Patient 
class MedicalNotes(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    patient_info = models.ForeignKey(PatientMedicalInfo, on_delete=models.CASCADE)
    doctor_notes = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Doctor notes after Meeting with the Patient {self.patient_name.first_name} {self.patient_name.last_name} {self.patient_info.weight} {self.patient_info.height} {self.patient_info.blood_pressure} {self.doctor_notes} {self.doctor.last_name}"