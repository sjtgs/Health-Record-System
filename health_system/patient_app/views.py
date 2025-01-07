# patient_app/views.py
from django.contrib.auth.decorators import login_required
from patient_app.decorators import roles_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import os
from rest_framework import viewsets
from patient_app.serializers import PatientSerializer
from patient_app.models import Patient, OCRData

from patient_app.forms import OCRImageUploadForm
from patient_app.utils import extract_text_from_image
from google.cloud import vision
from django.conf import settings

@login_required
@roles_required
def view_patient_records(request):
    # Get the currently logged-in patient
    current_patient = request.user.patient

    # Fetch records for the current patient
    patient_records = Patient.objects.filter(user=request.user)

    return render(
        request,
        "patient_website/patient_records.html",
        {"patient_records": patient_records},
    )


# This API Funtion Displays the list of Patient Records
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@login_required
@roles_required
def patient_detail(request, auto_id):
    logged_in_user = request.user
    patient_detail = get_object_or_404(Patient, auto_id=auto_id)
    if logged_in_user != patient_detail.user:
        return render(request, "website/forbidden_page.html", status=403)
    return render(
        request,
        "patient_website/patient_detail.html",
        {"patient_detail": patient_detail},
    )


# Testing OCR view 
def extract_text_from_image(image_path):
    # Google Vision API text extraction logic
    client = vision.ImageAnnotatorClient()
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
        image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description if texts else "No text found"

def upload_and_extract_text(request):
    if request.method == 'POST':
        form = OCRImageUploadForm(request.POST, request.FILES)
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
            OCRData.objects.create(
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
        form = OCRImageUploadForm()

    return render(request, 'patient_website/patient_ocr.html', {'form': form})
