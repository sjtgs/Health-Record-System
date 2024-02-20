# patient_app/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import PatientLoginForm, PatientForm
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
    patient_lists = Patient.objects.all()
    return render(
        request, "patient_website/patient_list.html", {"patient_lists": patient_lists}
    )


# This API Funtion Displays the list of Patient Records


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


# The function Creates a user based on the information Entered
@login_required
def patient_form(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("patient-lists")
    else:
        form = PatientForm()
    return render(request, "patient_website/patient_form.html", {"form": form})


@login_required
def patient_form_edit(request, auto_id):
    post = get_object_or_404(Patient, auto_id=auto_id)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(
                "patient-lists",
            )
    else:
        form = PatientForm(instance=post)
    return render(request, "patient_website/patient_form.html", {"form": form})


@login_required
def patient_detail(request, auto_id):
    patient_detail = get_object_or_404(Patient, auto_id=auto_id)
    return render(
        request,
        "patient_website/patient_detail.html",
        {"patient_detail": patient_detail},
    )


# def is_patient(user):
#     return user.groups.filter(name="Patients").exists()


# @user_passes_test(is_patient)
# def view_patient_records(request):
#     # Your view logic for patients to view their records
#     return render(request, "patient_records.html")
