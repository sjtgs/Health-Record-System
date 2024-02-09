# Doctor_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet
from . import views

router = DefaultRouter()
router.register(r"doctors", DoctorViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("patient-lists/", views.PatientsLists, name="patient-lists"),
    path("doctor-lists/", views.DoctorLists, name="doctor-lists"),
    path("nurse-lists/", views.NurseLists, name="nurse-lists"),
]
