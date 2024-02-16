from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomePage, name="index"),
    path("dashboard/", views.Dashboard, name="dashboard"),
]
