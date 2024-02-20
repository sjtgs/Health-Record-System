# Nurse_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from nurse_app.views import (
    NurseViewSet,
    NurseLists,
    PatientLists,
    nurse_login,
    nurse_form,
    nurse_form_edit,
    nurse_detail,
    patient_detail,
)

nurse_router = DefaultRouter()
nurse_router.register(r"nurses", NurseViewSet)


urlpatterns = [
    path("nurses/", include(nurse_router.urls)),
    path("login/", nurse_login, name="nurse_login"),
    path("nurse-lists/", NurseLists, name="nurse-lists"),
    path("patient-lists/", PatientLists, name="nurse-lists"),
    path("nurse-form/", nurse_form, name="nurse-form"),
    path("<int:auto_id>/nurse-form-edit/", nurse_form_edit, name="nurse-form-edit"),
    path("nurse-detail/<int:auto_id>/", nurse_detail, name="nurse-detail"),
    path("patient-detail/<int:auto_id>/", patient_detail, name="patient-detail"),
]
