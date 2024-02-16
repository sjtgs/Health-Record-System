# nurse_app/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import NurseLoginForm
from rest_framework import viewsets
from nurse_app.serializers import NurseSerializer
from nurse_app.models import Nurse
from patient_app.models import Patient


def nurse_login(request):
    if request.method == "POST":
        form = NurseLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
        else:
            form = NurseLoginForm()
        return render(request, "nurse_website/nurse_login.html", {"form": form})


# This Function Displays the list of Entire Nurse Record in the Database
@login_required
def NurseLists(request):
    nurse_lists = Nurse.objects.all()
    return render(
        request, "nurse_website/nurse_lists.html", {"nurse_lists": nurse_lists}
    )


# This Function Display the list of Entire Patient Record in the Database
@login_required
def PatientLists(request):
    patient_lists = Patient.objects.all()
    return render(
        request, "nurse_website/patient_lists.html", {"patient_lists": patient_lists}
    )


# The API Funtion Displays the list of Nurse Records


class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
