from django import forms
from appointment_app.models import Appointment, PatientMedicalInfo , MedicalNotes


# Created Appointment forms
class AppointmentForms(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["date", "time", "reason"]

# Created Patient Medical Information Form 
class PatientMedicalInfoForms(forms.ModelForm):
    class Meta:
        model = PatientMedicalInfo
        fields = ["patient", "weight", "height", "blood_pressure"]


# Created Doctors Medical Notes 
class MedicalNotesForm(forms.Form):
    patient_id = forms.ModelChoiceField(
        queryset=MedicalNotes.objects.all(),
        to_field_name = "auto_id",
        empty_label= "Select a Patient"
    )
    image = forms.ImageField()