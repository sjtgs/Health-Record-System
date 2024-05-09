from django.urls import path
from . import views
from dashboard_app.views import appointment_review, appointment_review_detail


urlpatterns = [
    path("", views.HomePage, name="index"),
    path("appointment-review/", appointment_review, name="appointment-review"),
    path(
        "appointment-review-detail/<int:appointment_id>/",
        appointment_review_detail,
        name="appointment-review-detail",
    ),
]
