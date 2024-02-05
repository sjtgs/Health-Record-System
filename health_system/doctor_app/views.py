from django.shortcuts import render
from patient_app.models import Patient


# Show the List the of the Patient Records
def PatientsLists(request):
    patients = Patient.objects.all()
    return render(request, "website/patient_lists.html", {"patients": patients})
