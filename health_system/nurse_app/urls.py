from django.urls import path
from . import views

# from nurse_app.views import NurseLists,Patient


urlpatterns = [
    path("nurse-lists/", views.NurseLists, name="nurse-lists"),
    path("patient-lists/", views.PatientLists, name="nurse-lists"),
]
