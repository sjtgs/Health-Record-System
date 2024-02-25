from django.contrib.auth.decorators import login_required
from administration_app.decorators import admin_role_required
from doctor_app.decorators import doctor_role_required
from nurse_app.decorators import role_required
from patient_app.decorators import roles_required
from django.shortcuts import render
from doctor_app.models import Doctor
from nurse_app.models import Nurse
from patient_app.models import Patient
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
    # Query the Doctor model to get the count of doctors for specialization
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


# This Function Displays the list of Entire Doctor Lists in the Database
@login_required
@doctor_role_required
def doctor_lists(request):
    doctor_lists = Doctor.objects.all()
    return render(
        request,
        "administration_website/doctor_lists.html",
        {"doctor_lists": doctor_lists},
    )


# This Function Displays the list of Entire Nurse Lists in the Database
@login_required
@role_required
def nurse_lists(request):
    nurse_lists = Nurse.objects.all()
    return render(
        request,
        "administration_website/nurse_lists.html",
        {"nurse_lists": nurse_lists},
    )


@login_required
@roles_required
def patient_lists(request):
    patient_lists = Patient.objects.all()
    return render(
        request,
        "administration_website/patient_list.html",
        {"patient_lists": patient_lists},
    )
