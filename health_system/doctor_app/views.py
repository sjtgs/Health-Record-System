from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from forms import DoctorLoginForm
from rest_framework import viewsets
from doctor_app.serializers import DoctorSerializer
from doctor_app.models import Doctor
from patient_app.models import Patient
from nurse_app.models import Nurse


def doctor_login(request):
    if request.method == "POST":
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
        else:
            form = DoctorLoginForm()
        return render(request, "doctor_website/doctor_login.html", {"form": form})


# This Function Displays the list of Entire Doctor Record in the Database
def DoctorLists(request):
    doctor_lists = Doctor.objects.all()
    return render(
        request, "doctor_website/doctor_lists.html", {"doctor_lists": doctor_lists}
    )


# This Function Displays the list of Entire Patient Record in the Database# Show the List the of the Patient Records
def PatientsLists(request):
    patient_lists = Patient.objects.all()
    return render(
        request, "doctor_website/patient_lists.html", {"patient_lists": patient_lists}
    )


# This Function Displays the list of Entire Nurse Record in the Database
def NurseLists(request):
    nurse_lists = Nurse.objects.all()
    return render(
        request, "doctor_website/nurse_lists.html", {"nurse_lists": nurse_lists}
    )


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
