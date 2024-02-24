# nurse_app/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from nurse_app.decorators import role_required
from nurse_app.forms import NurseForm
from rest_framework import viewsets
from nurse_app.serializers import NurseSerializer
from nurse_app.models import Nurse
from patient_app.models import Patient


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


# The function Creates a user based on the information Entered
@login_required
def nurse_form(request):
    if request.method == "POST":
        form = NurseForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("nurse-lists")
    else:
        form = NurseForm()
    return render(request, "nurse_website/nurse_form.html", {"form": form})


@login_required
def nurse_form_edit(request, auto_id):
    post = get_object_or_404(Nurse, auto_id=auto_id)
    if request.method == "POST":
        form = NurseForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(
                "nurse-lists",
            )
    else:
        form = NurseForm(instance=post)
    return render(request, "nurse_website/nurse_form.html", {"form": form})


@login_required
def nurse_detail(request, auto_id):
    nurse_detail = get_object_or_404(Nurse, auto_id=auto_id)
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
