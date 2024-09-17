from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from patient_app.models import Patient
from appointment_app.models import Appointment
from appointment_app.forms import AppointmentForms


# Create Schedule Appointment Function
@login_required
def schedule_appointment(request, auto_id):
    patient = Patient.objects.get(auto_id=auto_id)
    if request.method == "POST":
        form = AppointmentForms(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.doctor = request.user
            appointment.save()
            return redirect(
                "administration_website/patient_detail", auto_id=patient.auto_id
            )
        else:
            form = AppointmentForms()
        return render(
            request,
            "administration_website/schedule_appointment.html",
            {"form": form, "patient": patient},
        )


# Create a Funtion to list appointment events
def appointment_events(request):
    appointments = Appointment.objects.all()
    events = []

    for appointment in appointments:
        events.append(
            {
                "title": f"{appointment.patient.first_name} {appointment.patient.last_name}",
                "start": f"{appointment.date}T{appointment.time}",
                "description": appointment.reason,
            }
        )
        return JsonResponse(events, safe=False)
