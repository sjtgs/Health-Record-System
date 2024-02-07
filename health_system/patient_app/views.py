# patient_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group


def is_patient(user):
    return user.groups.filter(name="Patients").exists()


@user_passes_test(is_patient)
def view_patient_records(request):
    # Your view logic for patients to view their records
    return render(request, "patient_records.html")
