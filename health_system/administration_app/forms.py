from django import forms
from administration_app.models import Administrator
from doctor_app.models import Doctor
from nurse_app.models import Nurse
from patient_app.models import Patient


# Administrator User Form
class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = "__all__"
        widgets = {
            "date_of_birth": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Date of Birth",
                    "type": "date",
                },
            ),
        }
        exclude = (
            "user",
            "group",
            "auto_id",
            "created_by",
            "updated_at",
        )


# Doctor User Form
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        widgets = {
            "date_of_birth": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Date of Birth",
                    "type": "date",
                },
            ),
        }
        exclude = (
            "user",
            "group",
            "auto_id",
            "created_by",
            "updated_at",
        )


# Upload Doctor CSV / EXCEL FILE
class DoctorUploadForm(forms.Form):
    file = forms.FileField(label="Select a File ")


# Nurse User Form
class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = "__all__"
        widgets = {
            "date_of_birth": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Date of Birth",
                    "type": "date",
                },
            ),
        }
        exclude = (
            "user",
            "group",
            "auto_id",
            "created_by",
            "updated_at",
        )


# Upload Nurse CSV / EXCEL FILE
class NurseUploadForm(forms.Form):
    file = forms.FileField(label="Select a File ")


# Patient User Form
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        widgets = {
            "date_of_birth": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Date of Birth",
                    "type": "date",
                },
            ),
        }
        exclude = (
            "user",
            "group",
            "auto_id",
            "created_by",
            "updated_at",
        )


# Upload Patient CSV / EXCEL FILE
class PatientUploadForm(forms.Form):
    file = forms.FileField(label="Select a File ")
