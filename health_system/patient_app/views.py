# patient_app/views.py
from django.contrib.auth.decorators import login_required
from patient_app.decorators import roles_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from patient_app.serializers import PatientSerializer
from patient_app.models import Patient, OCRData
from patient_app.forms import OCRImageUploadForm
from patient_app.utils import extract_text_from_image


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
def upload_and_extract_text(request):
    if request.method == 'POST':
        form = OCRImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            patient_id = form.cleaned_data['patient_id']
            image = form.cleaned_data['image']

            # Save the image temporarily
            image_path = f"uploads/{image.name}"
            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            # Extract text using Google Vision API
            extracted_text = extract_text_from_image(image_path)

            # Save to database
            patient = get_object_or_404(Patient, id=patient_id)
            OCRData.objects.create(patient=patient, extracted_text=extracted_text)

            # Clean up the temporary file
            os.remove(image_path)

            return JsonResponse({
                "message": "Text extracted and saved successfully",
                "extracted_text": extracted_text
            })

    else:
        form = OCRImageUploadForm()

    return render(request, 'patient_website/patient_ocr.html', {'form': form})
