from django.urls import path
from . import views


urlpatterns = [
    path("nurse-list/", views.NurseLists, name="nurse-list"),
]
