from django.shortcuts import render
from .models import InsuranceCompany


def InsuranceLists(request):
    insurance_companies = InsuranceCompany.objects.all()
    return render(
        request,
        "website/insurance-list.html",
        {"insurance_companies": insurance_companies},
    )
