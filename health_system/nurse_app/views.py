from django.shortcuts import render
from rest_framework import viewsets
from nurse_app.serializers import NurseSerializer
from nurse_app.models import Nurse
from patient_app.models import Patient


# This Function Displays the list of Entire Nurse Record in the Database
def NurseLists(request):
    nurse_lists = Nurse.objects.all()
    return render(
        request, "nurse_website/nurse_lists.html", {"nurse_lists": nurse_lists}
    )


# This Function Display the list of Entire Patient Record in the Database
def PatientLists(request):
    patient_lists = Patient.objects.all()
    return render(
        request, "nurse_website/patient_lists.html", {"patient_lists": patient_lists}
    )


class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
