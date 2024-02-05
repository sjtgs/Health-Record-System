# Doctor_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("patient-list/", views.PatientsLists, name="patient-list"),
]
