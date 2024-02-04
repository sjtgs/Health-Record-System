from django.urls import path
from . import views


urlpatterns = [
    path("nurse/", views.NurseHome, name="nurse"),
]
