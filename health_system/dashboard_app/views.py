from django.shortcuts import render
from patient_app.models import Patient
from .models import PatientReview


def Home(request):
    patients_reviews = PatientReview.objects.all()
    patients = Patient.objects.all()
    return render(
        request,
        "dashboard/index.html",
        {"patients": patients, "patients_reviews": patients_reviews},
    )
