# Nurse_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from nurse_app.views import NurseViewSet, NurseLists, PatientLists, nurse_login

nurse_router = DefaultRouter()
nurse_router.register(r"nurses", NurseViewSet)


urlpatterns = [
    path("nurses/", include(nurse_router.urls)),
    path("login/", nurse_login, name="nurse_login"),
    path("nurse-lists/", NurseLists, name="nurse-lists"),
    path("patient-lists/", PatientLists, name="nurse-lists"),
]
