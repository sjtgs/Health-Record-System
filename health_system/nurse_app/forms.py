from django import forms
from nurse_app.models import Nurse


class NurseLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = "__all__"
        exclude = (
            "user",
            "auto_id",
            "created_by",
            "updated_at",
        )
