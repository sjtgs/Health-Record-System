from django.shortcuts import render, redirect
from dashboard_app.models import AppointmentReview
from dashboard_app.forms import AppointmentReviewForm
from dashboard_app.logger_review import log_patient_review_appointment


def HomePage(request):
    return render(request, "website/index.html", {})


# Appointment Review Form
def appointment_review(request):
    if request.method == "POST":
        form = AppointmentReviewForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            log_patient_review_appointment(appointment)
            return redirect("appointment-review-detail", appointment_id=appointment.id)
    else:
        form = AppointmentReviewForm()
    return render(request, "website/review_appointment.html", {"form": form})


def appointment_review_detail(request, appointment_id):
    appointment = AppointmentReview.objects.get(pk=appointment_id)
    return render(
        request,
        "website/appointment_review_detail.html",
        {"appointment": appointment},
    )
