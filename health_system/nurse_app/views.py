from django.shortcuts import render
from nurse_app.models import Nurse
from patient_app.models import Patient


# This Function Displays the list of Entire Nurse Record in the Database
def NurseLists(request):
    nurse_lists = Nurse.objects.all()
    return render(request, "website/nurse_lists.html", {"nurse_lists": nurse_lists})


# This Function Display the list of Entire Patient Record in the Database
def PatientLists(request):
    patient_lists = Patient.objects.all()
    return render(
        request, "website/patient_lists.html", {"patient_lists": patient_lists}
    )
