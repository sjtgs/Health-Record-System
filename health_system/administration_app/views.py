from django.contrib.auth.decorators import login_required
from administration_app.decorators import admin_role_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from administration_app.logger import (
    log_administrator_creation,
    log_doctor_creation,
    log_nurse_creation,
    log_patient_creation,
)

from django.shortcuts import redirect
from administration_app.models import Administrator

from doctor_app.models import Doctor
from nurse_app.models import Nurse
from patient_app.models import *
from administration_app.forms import (
    AdministratorForm,
    DoctorForm,
    DoctorUploadForm,
    NurseForm,
    NurseUploadForm,
    PatientForm,
    PatientUploadForm,
)
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import csv
from io import TextIOWrapper
import json


@login_required
@admin_role_required
def doctor_experience_chart(request):
    # Query the Doctor model to get the count of doctors for each years of experience
    experience_counts = Doctor.objects.values("years_of_experience").annotate(
        count=Count("auto_id")
    )

    # Prepare the data for the Pie chart
    labels = [item["years_of_experience"] for item in experience_counts]
    data = [item["count"] for item in experience_counts]

    return render(
        request,
        "administration_website/doctor_experience_chart.html",
        {"labels": labels, "data": data},
    )


@login_required
@admin_role_required
def doctor_specialization_chart(request):
    # Query the Doctor model to get the count of doctors for specialization
    specialization_counts = Doctor.objects.values("specialization").annotate(
        count=Count("auto_id")
    )
    # Prepare the data for the Bar chart
    labels = [item["specialization"] for item in specialization_counts]
    data = [item["count"] for item in specialization_counts]
    return render(
        request,
        "administration_website/doctor_specialization_chart.html",
        {"labels": labels, "data": data},
    )


# This Function Shows Doctor Gender Distribution and displays it as a Pie Chart
@login_required
@admin_role_required
def doctor_gender_distribution(request):
    male_count = Doctor.objects.filter(gender="M").count()
    female_count = Doctor.objects.filter(gender="F").count()
    labels = ["Male", "Female"]
    data = [male_count, female_count]

    return render(
        request,
        "administration_website/doctor_gender_pie_chart.html",
        {
            "labels": labels,
            "data": data,
        },
    )


# This Function Shows Nurse Gender Distribution and displays it as a Pie Chart
@login_required
@admin_role_required
def nurse_gender_distribution(request):
    male_nurse_count = Nurse.objects.filter(gender="M").count()
    female_nurse_count = Nurse.objects.filter(gender="F").count()
    labels = ["Male", "Female"]
    data = [male_nurse_count, female_nurse_count]

    return render(
        request,
        "administration_website/nurse_gender_distribution.html",
        {"labels": labels, "data": data},
    )


# This Function Shows Patient Gender Distribution and displays it as a Pie Chart
@login_required
@admin_role_required
def patient_gender_distribution(request):
    male_patient_count = Patient.objects.filter(gender="M").count()
    female_patient_count = Patient.objects.filter(gender="F").count()

    labels = ["Male", "Female"]
    data = [male_patient_count, female_patient_count]

    return render(
        request,
        "administration_website/patient_gender_distribution.html",
        {"labels": labels, "data": data},
    )


@login_required
@admin_role_required
def view_all_records(request):
    doctors_records = Doctor.objects.all()
    nurse_record = Nurse.objects.all()
    patient_record = Patient.objects.all()
    # Query the Doctor model to get the count of doctors for specialization
    specialization_counts = Doctor.objects.values("specialization").annotate(
        count=Count("auto_id")
    )
    # Prepare the data for the Pie chart
    labels = [item["specialization"] for item in specialization_counts]
    data = [item["count"] for item in specialization_counts]
    # Query the Doctor model to get the count of doctors for specializationHe
    specializations_counts = Doctor.objects.values("specialization").annotate(
        count=Count("auto_id")
    )

    # Prepare the data for the bar chart
    label = [item["specialization"] for item in specializations_counts]
    datas = [item["count"] for item in specializations_counts]

    page = request.GET.get("page", 1)
    paginator = Paginator(nurse_record, 10)
    patient_paginatior = Paginator(patient_record, 10)
    patient_page = request.GET.get("patient_page", 1)

    try:
        nurses_records = paginator.page(page)
    except PageNotAnInteger:
        nurses_records = paginator.page(1)
    except EmptyPage:
        nurses_records = paginator.page(paginator.num_pages)

    try:
        patients_records = patient_paginatior.page(patient_page)
    except PageNotAnInteger:
        patients_records = patient_paginatior.page(1)
    except EmptyPage:
        patients_records = patient_paginatior.page(patient_paginatior.num_pages)

    return render(
        request,
        "administration_website/admin_dashboard.html",
        {
            "doctors_records": doctors_records,
            "nurses_records": nurses_records,
            "patients_records": patients_records,
            "labels": labels,
            "data": data,
            "label": label,
            "datas": datas,
        },
    )


# This Function Displays the list of Entire Doctors Lists in the Database
@login_required
@admin_role_required
def doctor_lists(request):
    doctor_lists = Doctor.objects.all()
    return render(
        request,
        "administration_website/doctor_lists.html",
        {"doctor_lists": doctor_lists},
    )


# This Function Displays the list of Entire Nurses Lists in the Database
@login_required
@admin_role_required
def nurse_lists(request):
    nurse_lists = Nurse.objects.all()
    return render(
        request,
        "administration_website/nurse_lists.html",
        {"nurse_lists": nurse_lists},
    )


# This Function Displays the list of Entire Patients Lists in the Database
@login_required
@admin_role_required
def patient_lists(request):
    patient_lists = Patient.objects.all()
    return render(
        request,
        "administration_website/patient_list.html",
        {"patient_lists": patient_lists},
    )


# The Function Creates a Administrator User based on the information Entered.
@login_required
@admin_role_required
def administrator_form(request):
    if request.method == "POST":
        form = AdministratorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            log_administrator_creation(post)
            return redirect("administrator-detail", auto_id=post.auto_id)
    else:
        form = AdministratorForm()
    return render(
        request, "administration_website/administration_form.html", {"form": form}
    )


# The Function Edits a Administration Information.
@login_required
@admin_role_required
def administrator_form_edit(request, auto_id):
    post = get_object_or_404(Administrator, auto_id=auto_id)
    if request.method == "POST":
        form = AdministratorForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("administrator-detail", auto_id=post.auto_id)
    else:
        form = DoctorForm(instance=post)
    return render(
        request, "administration_website/administration_form.html", {"form": form}
    )


# The Function a Administration Detail.
@login_required
@admin_role_required
def admin_administrator_detail(request, auto_id):
    administrator_detail = get_object_or_404(Administrator, auto_id=auto_id)
    return render(
        request,
        "administration_website/administration_detail.html",
        {"administrator_detail": administrator_detail},
    )


# The Function Creates a Doctor User based on the information Entered.
@login_required
@admin_role_required
def doctor_form(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            log_doctor_creation(post)
            # Redirect to admin-doctor-detail with auto_id parameter
            return redirect("admin-doctor-detail", auto_id=post.auto_id)
    else:
        form = DoctorForm()
    return render(request, "administration_website/doctor_form.html", {"form": form})


# The Function Edits a Doctors Information.
@login_required
@admin_role_required
def doctor_form_edit(request, auto_id):
    post = get_object_or_404(Doctor, auto_id=auto_id)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("admin-doctor-detail/", auto_id=auto_id)
    else:
        form = DoctorForm(instance=post)
    return render(request, "administration_website/doctor_form.html", {"form": form})


# The Function shows Doctor Detail.
@login_required
@admin_role_required
def admin_doctor_detail(request, auto_id):
    doctor_detail = get_object_or_404(Doctor, auto_id=auto_id)
    return render(
        request,
        "administration_website/doctor_detail.html",
        {"doctor_detail": doctor_detail},
    )


# Uploading Doctor User
@login_required
@admin_role_required
def upload_doctor_file(request):
    if request.method == "POST":
        form = DoctorUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = TextIOWrapper(request.FILES["file"].file, encoding="utf-8")
            reader = csv.DictReader(file)
            for row in reader:
                doctor = Doctor(
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    date_of_birth=row["date_of_birth"],
                    gender=row["gender"],
                    nrc=row["nrc"],
                    countries_id=row["countries_id"],
                    provinces_id=row["provinces_id"],
                    towns_id=row["towns_id"],
                    address=row["address"],
                    medical_number=row["medical_number"],
                    hospitals_id=row["hospitals_id"],
                    specialization=row["specialization"],
                    years_of_experience=row["years_of_experience"],
                    email=row["email"],
                    phone_number=row["phone_number"],
                )
                doctor.save()
            return HttpResponse("File uploaded successfully.")
    else:
        form = NurseUploadForm()
    return render(
        request, "administration_website/upload_doctor_file.html", {"form": form}
    )


# The Function Creates a Nurse User based on the information Entered
@login_required
@admin_role_required
def nurse_form(request):
    if request.method == "POST":
        form = NurseForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            log_nurse_creation(post)
            return redirect("admin-nurse-detail", auto_id=post.auto_id)
    else:
        form = NurseForm()
    return render(request, "administration_website/nurse_form.html", {"form": form})


# The Function Edits a Nurses Information.
@login_required
@admin_role_required
def nurse_form_edit(request, auto_id):
    post = get_object_or_404(Nurse, auto_id=auto_id)
    if request.method == "POST":
        form = NurseForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("admin-nurse-detail", auto_id=post.auto_id)
    else:
        form = NurseForm(instance=post)
    return render(request, "administration_website/nurse_form.html", {"form": form})


# The Function shows Nurse Detail.
@login_required
@admin_role_required
def admin_nurse_detail(request, auto_id):
    nurse_detail = get_object_or_404(Nurse, auto_id=auto_id)
    return render(
        request,
        "administration_website/nurse_detail.html",
        {"nurse_detail": nurse_detail},
    )


# Uploading Nurse User
@login_required
@admin_role_required
def upload_nurse_file(request):
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
    return render(
        request, "administration_website/upload_nurse_file.html", {"form": form}
    )


# The Function Creates a Nurse User based on the information Entered
@login_required
@admin_role_required
def patient_form(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            log_patient_creation(post)
            return redirect("admin-patient-detail", auto_id=post.auto_id)
    else:
        form = PatientForm()
    return render(request, "administration_website/patient_form.html", {"form": form})


# The Function Edits a Nurses Information.
@login_required
@admin_role_required
def patient_form_edit(request, auto_id):
    post = get_object_or_404(Patient, auto_id=auto_id)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("admin-patient-detail", auto_id=post.auto_id)
    else:
        form = PatientForm(instance=post)
    return render(request, "administration_website/patient_form.html", {"form": form})


@login_required
@admin_role_required
def admin_patient_detail(request, auto_id):
    patient_detail = get_object_or_404(Patient, auto_id=auto_id)
    return render(
        request,
        "administration_website/patient_detail.html",
        {"patient_detail": patient_detail},
    )


# Uploading Patient User
@login_required
@admin_role_required
def upload_patient_file(request):
    if request.method == "POST":
        form = PatientUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = TextIOWrapper(request.FILES["file"].file, encoding="utf-8")
            reader = csv.DictReader(file)
            for row in reader:
                # Get or create related objects for foreign key fields
                province = get_object_or_404(Province, pk=row["province_id"])
                town = get_object_or_404(Town, pk=row["town_id"])
                hospital = get_object_or_404(MedicalInformation, pk=row["hospital_id"])
                diagnosis = get_object_or_404(Diagnosis, pk=row["diagnosis_id"])
                insurance = get_object_or_404(InsuranceCompany, pk=row["insurance_id"])

                # Create a new Patient instance and populate its fields from the CSV row
                patient = Patient(
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    date_of_birth=row["date_of_birth"],
                    gender=row["gender"],
                    nrc=row["nrc"],
                    patient_type=row["patient_type"],
                    provinces=province,
                    towns=town,
                    address=row["address"],
                    hospitals=hospital,
                    medical_history=row["medical_history"],
                    blood_type=row["blood_type"],
                    diagnosis=diagnosis,
                    patient_unit=row["patient_unit"],
                    treatment_plan=row["treatment_plan"],
                    prescription=row["prescription"],
                    insurance=insurance,
                    email=row["email"],
                    phone_number=row["phone_number"],
                )
                patient.save()

            return HttpResponse("File uploaded successfully.")
    else:
        form = PatientUploadForm()
    return render(
        request, "administration_website/upload_patient_file.html", {"form": form}
    )
