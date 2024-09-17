# Nurse_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from nurse_app.views import (
    NurseViewSet,
    view_nurse_record,
    patient_records,
    # nurse_dashboard,
    nurse_detail,
    patient_detail,
    # appointment_detail,
    # book_appointment,
)

nurse_router = DefaultRouter()
nurse_router.register(r"nurses", NurseViewSet)


urlpatterns = [
    path("nurses/", include(nurse_router.urls)),
    # path("nurse-dashboard/", view_nurse_record, name="nurse-dashboard"),
    path("nurse-record/", view_nurse_record, name="nurse-record"),
    path("patient-records/", patient_records, name="patient-records"),
    path("nurse-detail/<int:auto_id>/", nurse_detail, name="nurse-detail"),
    path("patient-detail/<int:auto_id>/", patient_detail, name="patient-detail"),
]
