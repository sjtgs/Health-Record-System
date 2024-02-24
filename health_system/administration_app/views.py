from django.contrib.auth.decorators import login_required
from doctor_app.decorators import doctor_role_required
from nurse_app.decorators import role_required
from patient_app.decorators import roles_required
from django.shortcuts import render
from doctor_app.models import Doctor
from nurse_app.models import Nurse
from patient_app.models import Patient


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
