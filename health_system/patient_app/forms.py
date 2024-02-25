from django import forms
from patient_app.models import Patient


# Patient Form
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        exclude = (
            "user",
            "group",
            "auto_id",
            "created_by",
            "updated_at",
        )
