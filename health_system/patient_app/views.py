# patient_app/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from forms import PatientLoginForm
from rest_framework import viewsets
from patient_app.serializers import PatientSerializer
from patient_app.models import Patient

# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.models import Group


def patient_login(request):
    if request.method == "POST":
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
        else:
            form = PatientLoginForm()
        return render(request, "patient_website/patient_login.html", {"form": form})


@login_required
def PatientLists(request):
    parent_lists = Patient.objects.all()
    return render(
        request, "patient_website/patient_list.html", {"parent_lists": parent_lists}
    )


# This API Funtion Displays the list of Patient Records
@login_required
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


# def is_patient(user):
#     return user.groups.filter(name="Patients").exists()


# @user_passes_test(is_patient)
# def view_patient_records(request):
#     # Your view logic for patients to view their records
#     return render(request, "patient_records.html")
