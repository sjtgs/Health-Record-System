from django.urls import path
from . import views

urlpatterns = [
    path("insurance-list/", views.InsuranceLists, name="insurance-list"),
]
