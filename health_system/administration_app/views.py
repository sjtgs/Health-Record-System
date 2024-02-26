from django.contrib.auth.decorators import login_required
from administration_app.decorators import admin_role_required
from doctor_app.decorators import doctor_role_required
from nurse_app.decorators import role_required
from patient_app.decorators import roles_required
from django.shortcuts import render, redirect, get_object_or_404
from administration_app.models import Administrator
from doctor_app.models import Doctor
from nurse_app.models import Nurse
from patient_app.models import Patient
from administration_app.forms import (
    AdministratorForm,
    DoctorForm,
    NurseForm,
    PatientForm,
)
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    paginator = Paginator(nurse_record, 2)
    patient_paginatior = Paginator(patient_record, 2)
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
@doctor_role_required
def doctor_lists(request):
    doctor_lists = Doctor.objects.all()
    return render(
        request,
        "administration_website/doctor_lists.html",
        {"doctor_lists": doctor_lists},
    )


# This Function Displays the list of Entire Nurses Lists in the Database
@login_required
@role_required
def nurse_lists(request):
    nurse_lists = Nurse.objects.all()
    return render(
        request,
        "administration_website/nurse_lists.html",
        {"nurse_lists": nurse_lists},
    )


# This Function Displays the list of Entire Patients Lists in the Database
@login_required
@roles_required
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
            return redirect("administrator-detail")
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
            return redirect(
                "administrator-detail",
            )
    else:
        form = DoctorForm(instance=post)
    return render(
        request, "administration_website/administration_form.html", {"form": form}
    )


# The Function Creates a Doctor User based on the information Entered.
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


# The Function Edits a Doctors Information.
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


# The Function Creates a Nurse User based on the information Entered
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


# The Function Edits a Nurses Information.
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


# The Function Creates a Nurse User based on the information Entered
@login_required
@roles_required
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


# The Function Edits a Nurses Information.
@login_required
@roles_required
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
@admin_role_required
def admin_patient_detail(request, auto_id):
    patient_detail = get_object_or_404(Patient, auto_id=auto_id)
    return render(
        request,
        "administration_website/patient_detail.html",
        {"patient_detail": patient_detail},
    )
