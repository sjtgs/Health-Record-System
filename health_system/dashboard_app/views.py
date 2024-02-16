from django.shortcuts import render
from patient_app.models import Patient
from .models import PatientReview


def HomePage(request):
    return render(request, "website/index.html", {})


def Dashboard(request):
    patients_reviews = PatientReview.objects.all()
    patient_lists = Patient.objects.all()
    return render(
        request,
        "website/dashboard.html",
        {"patient_lists": patient_lists, "patients_reviews": patients_reviews},
    )
