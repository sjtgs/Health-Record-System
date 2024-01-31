from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(Province)
admin.site.register(Town)
admin.site.register(MedicalInformation)
admin.site.register(Diagnosis)
admin.site.register(Patient)
admin.site.register(PatientImage)
