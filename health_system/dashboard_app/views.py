from django.shortcuts import render
from patient_app.models import Patient
from .models import PatientReview


def Home(request):
    patients_reviews = PatientReview.objects.all()
    patient_lists = Patient.objects.all()
    return render(
        request,
        "website/index.html",
        {"patient_lists": patient_lists, "patients_reviews": patients_reviews},
    )
