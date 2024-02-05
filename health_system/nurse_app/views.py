from django.shortcuts import render
from .models import Nurse


# Show the List the of the Nurse Records
def NurseLists(request):
    nurses = Nurse.objects.all()
    return render(request, "website/nurse_list.html", {"nurses": nurses})
