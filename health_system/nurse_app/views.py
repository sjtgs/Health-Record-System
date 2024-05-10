# nurse_app/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from nurse_app.decorators import role_required
from rest_framework import viewsets
from nurse_app.serializers import NurseSerializer
from nurse_app.logger import log_patient_book_appointment
from nurse_app.models import Nurse, Appointment
from patient_app.models import Patient
from nurse_app.forms import NurseUploadForm, AppointmentForm
import csv
from io import TextIOWrapper


# This Function Displays the list of Entire Patient Record in the Database
@login_required
@role_required
def patient_records(request):
    patient_records = Patient.objects.all()
    return render(
        request,
        "nurse_website/patient_records.html",
        {"patient_records": patient_records},
    )


# This Function Displays the list of Entire Nurse Record in the Database
@login_required
@role_required
def view_nurse_record(request):
    current_nurse = request.user.nurse
    nurse_record = Nurse.objects.filter(user=request.user)
    return render(
        request, "nurse_website/nurse_record.html", {"nurse_record": nurse_record}
    )


@login_required
def nurse_detail(request, auto_id):
    logged_in_user = request.user
    nurse_detail = get_object_or_404(Nurse, auto_id=auto_id)
    if logged_in_user != nurse_detail.user:
        return render(request, "website/forbidden_page.html", status=403)
    return render(
        request, "nurse_website/nurse_detail.html", {"nurse_detail": nurse_detail}
    )


@login_required
def patient_detail(request, auto_id):
    patient_detail = get_object_or_404(Patient, auto_id=auto_id)
    return render(
        request, "nurse_website/patient_detail.html", {"patient_detail": patient_detail}
    )


# The API Funtion Displays the list of Nurse Records
class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer


# Booking Appointment Form


def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.nurse = request.user.nurse
            appointment.save()
            log_patient_book_appointment(appointment)
            return redirect("appointment_detail", appointment_id=appointment.id)
    else:
        form = AppointmentForm()
    return render(request, "nurse_website/book_appointment.html", {"form": form})


def appointment_detail(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    return render(
        request, "nurse_website/appointment_detail.html", {"appointment": appointment}
    )


# Uploading Nurse User
def upload_nurse(request):
    if request.method == "POST":
        form = NurseUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = TextIOWrapper(request.FILES["file"].file, encoding="utf-8")
            reader = csv.DictReader(file)
            for row in reader:
                nurse = Nurse(
                    first_name=row["First Name"],
                    last_name=row["Last Name"],
                    date_of_birth=row["Date of Birth"],
                    gender=row["Gender"],
                    nrc=row["NRC"],
                    countries_id=row["Country"],
                    provinces_id=row["Province"],
                    towns_id=row["Town"],
                    address=row["Address"],
                    medical_number=row["Medical Number"],
                    hospitals_id=row["Hospital"],
                    specialization=row["Specialization"],
                    years_of_experience=row["Years of Experience"],
                    email=row["Email"],
                    phone_number=row["Phone Number"],
                )
                nurse.save()
            return HttpResponse("File uploaded successfully.")
    else:
        form = NurseUploadForm()
    return render(request, "nurse_website/upload_nurse.html", {"form": form})
