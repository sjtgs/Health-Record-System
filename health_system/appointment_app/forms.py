from django import forms
from appointment_app.models import Appointment, PatientMedicalInfo , MedicalNotes
from patient_app.models import Patient


# Created Appointment forms
class AppointmentForms(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["patient","date", "time", "reason"]

# Created Patient Medical Information Form 
class PatientMedicalInfoForms(forms.ModelForm):
    class Meta:
        model = PatientMedicalInfo
        fields = ["patient", "weight", "height", "blood_pressure", "hiv_status"]


# Created Doctors Medical Notes 
class MedicalNotesForm(forms.Form):
    patient_name = forms.ModelChoiceField(
        queryset=Patient.objects.all(),  # Fetch all patients
        to_field_name="auto_id",              # Match the primary key (id) in the Patient model
        empty_label="Select a Patient",  # Optional placeholder for the dropdown
        label="Patient Name"             # Label displayed on the form
    )
    appointment_notes = forms.CharField(
        widget=forms.Textarea,          # Use a Textarea widget for multiline input
        label="Appointment Notes",      # Label for the field
        required=False                  # Make it optional if necessary
    )
    image = forms.ImageField(           # For uploading an image
        label="Upload Image",           # Label for the image field
        required=True                   # Mark the image field as required
    )


    def __init__(self, *args, patient_name=None, **kwargs):
        super().__init__(*args, **kwargs)
        if patient_name:
            self.fields["patient_name"].queryset = Patient.objects.filter(auto_id=patient_name)

