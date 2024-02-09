# Nurse_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NurseViewSet
from . import views

nurse_router = DefaultRouter()
nurse_router.register(r"nurses", NurseViewSet)


urlpatterns = [
    path("", include(nurse_router.urls)),
    path("nurse-lists/", views.NurseLists, name="nurse-lists"),
    path("patient-lists/", views.PatientLists, name="nurse-lists"),
]
