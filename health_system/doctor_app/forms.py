from django import forms
from doctor_app.models import Doctor


class DoctorLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        exclude = (
            "user",
            "auto_id",
            "created_by",
            "updated_at",
        )
