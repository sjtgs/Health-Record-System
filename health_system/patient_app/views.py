# patient_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from rest_framework import viewsets
from patient_app.serializers import PatientSerializer
from patient_app.models import Patient


def PatientLists(request):
    parent_lists = Patient.objects.all()
    return render(request, "website/patient_list.html", {"parent_lists": parent_lists})


def is_patient(user):
    return user.groups.filter(name="Patients").exists()


@user_passes_test(is_patient)
def view_patient_records(request):
    # Your view logic for patients to view their records
    return render(request, "patient_records.html")


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
