# Nurse_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NurseViewSet
from . import views

router = DefaultRouter()
router.register(r"nurses", NurseViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("nurse-lists/", views.NurseLists, name="nurse-lists"),
    path("patient-lists/", views.PatientLists, name="nurse-lists"),
]
