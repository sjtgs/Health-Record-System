from django.shortcuts import render, redirect
from django.http import JsonResponse , HttpResponse
import os
from django.contrib.auth.decorators import login_required
from patient_app.models import Patient
from appointment_app.models import Appointment, PatientMedicalInfo, MedicalNotes
from appointment_app.forms import AppointmentForms, PatientMedicalInfoForms , MedicalNotesForm
from appointment_app.utils import extract_text_from_image
from google.cloud import vision 
from django.conf import settings



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


#  Created Patient Medical Infomation Function
def patient_medical_info(request):
    patient_info = PatientMedicalInfo.objects.all()
    if request.method == "POST":
        form = PatientMedicalInfoForms(request.POST)
        if form.is_valid():
            patientInfo = form.save(commit=False)
            patientInfo.patient_info = patient_info
            patientInfo.save()
            return redirect(
                "appointment_website/patient_medical_info.html", 
            )
        else:
            form = PatientMedicalInfoForms()
        return render(
            request,
            "administration_website/schedule_appointment.html",
            {"form": form, "patient_info": patient_info},
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
    


# tHE Function below extract text from the image 
def extract_text_from_image(image_path):
    # Google Vision API text extraction logic
    client = vision.ImageAnnotatorClient()
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
        image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description if texts else "No text found"


# Upload and Extract OCR Data 
def upload_and_extract_text(request):
    if request.method == 'POST':
        form = MedicalNotesForm(request.POST, request.FILES)
        if form.is_valid():
            # Fetch the patient instance using the patient_id
            patient = form.cleaned_data['patient_id']  # This will return the selected Patient object
            
            # Process the uploaded image
            image = form.cleaned_data['image']
            image_path = f"images/{image.name}"
            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            # Extract text using Google Vision API
            extracted_text = extract_text_from_image(image_path)

            # Save the OCR data
            MedicalNotes.objects.create(
                patientdata=patient,
                extracted_note=extracted_text
            )

            # Clean up the temporary file
            os.remove(image_path)

            return JsonResponse({
                "message": "Text extracted and saved successfully",
                "extracted_text": extracted_text
            })
    else:
        form = MedicalNotesForm()

    return render(request, 'appointment_website/medical_notes.html', {'form': form})

