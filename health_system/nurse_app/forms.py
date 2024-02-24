from django import forms
from nurse_app.models import Nurse


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
