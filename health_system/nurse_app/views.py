from django.shortcuts import render
from .models import Nurse


def NurseHome(request):
    nurses = Nurse.objects.all()
    return render(request, "nurse/nurse_list.html", {"nurses": nurses})
