# patient_app/views.py
from django.contrib.auth.decorators import login_required
from patient_app.decorators import roles_required
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from patient_app.serializers import PatientSerializer
from patient_app.models import Patient


@login_required
@roles_required
def view_patient_records(request):
    # Get the currently logged-in patient
    current_patient = request.user.patient

    # Fetch records for the current patient
    patient_records = Patient.objects.filter(user=request.user)

    return render(
        request,
        "patient_website/patient_records.html",
        {"patient_records": patient_records},
    )


# This API Funtion Displays the list of Patient Records
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@login_required
@roles_required
def patient_detail(request, auto_id):
    patient_detail = get_object_or_404(Patient, auto_id=auto_id)
    return render(
        request,
        "patient_website/patient_detail.html",
        {"patient_detail": patient_detail},
    )
