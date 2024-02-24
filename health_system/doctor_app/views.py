# doctor_app/views.py

from django.contrib.auth.decorators import login_required
from doctor_app.decorators import doctor_role_required
from django.shortcuts import render, redirect, get_object_or_404
from doctor_app.forms import DoctorForm
from rest_framework import viewsets
from doctor_app.serializers import DoctorSerializer
from doctor_app.models import Doctor
from patient_app.models import Patient
from nurse_app.models import Nurse


@login_required
@doctor_role_required
def view_doctor_record(request):
    current_doctor = request.user.doctor
    doctor_record = Doctor.objects.filter(user=request.user)
    return render(
        request, "doctor_template/doctor_record.html", {"doctor_record": doctor_record}
    )


@login_required
@doctor_role_required
def doctor_dashboard(request):
    doctor_dashboard = Doctor.objects.all()
    return render(
        request,
        "doctor_website/doctor_dashboard.html",
        {"doctor_dashboard": doctor_dashboard},
    )


# This Function Displays the list of Entire Patient Record in the Database# Show the List the of the Patient Records


@login_required
@doctor_role_required
def PatientsLists(request):
    patient_lists = Patient.objects.all()
    return render(
        request, "doctor_website/patient_lists.html", {"patient_lists": patient_lists}
    )


# This Function Displays the list of Entire Nurse Record in the Database
@login_required
@doctor_role_required
def NurseLists(request):
    nurse_lists = Nurse.objects.all()
    return render(
        request, "doctor_website/nurse_lists.html", {"nurse_lists": nurse_lists}
    )


# The function Creates a user based on the information Entered
@login_required
@doctor_role_required
def doctor_form(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("doctor-detail")
    else:
        form = DoctorForm()
    return render(request, "doctor_website/doctor_form.html", {"form": form})


@login_required
@doctor_role_required
def doctor_form_edit(request, auto_id):
    post = get_object_or_404(Doctor, auto_id=auto_id)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(
                "doctor-detail",
            )
    else:
        form = DoctorForm(instance=post)
    return render(request, "doctor_website/doctor_form.html", {"form": form})


@login_required
@doctor_role_required
# Detail of the Doctor
def doctor_detail(request, auto_id):
    doctor_detail = get_object_or_404(Doctor, auto_id=auto_id)
    return render(
        request, "doctor_website/doctor_detail.html", {"doctor_detail": doctor_detail}
    )


@login_required
@doctor_role_required
# Details of the Patient
def patient_detail(request, auto_id):
    patient_detail = get_object_or_404(Patient, auto_id=auto_id)
    return render(
        request,
        "doctor_website/patient_detail.html",
        {"patient_detail": patient_detail},
    )


@login_required
@doctor_role_required
# Details of the Nurse
def nurse_detail(request, auto_id):
    nurse_detail = get_object_or_404(Nurse, auto_id=auto_id)
    return render(
        request, "doctor_website/nurse_detail.html", {"nurse_detail": nurse_detail}
    )


# This API function that displays the list Entire Doctors Records


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
