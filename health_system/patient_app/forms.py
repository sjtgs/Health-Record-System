from django import forms
from patient_app.models import Patient


class PatientLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


# Patient Form
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        exclude = (
            "user",
            "auto_id",
            "created_by",
            "updated_at",
        )
