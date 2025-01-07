from google.cloud import vision
import os

# Set up Google Cloud credentials
def extract_text_from_image(image_path):
    """Uses Google Cloud Vision API to extract text from an image."""
    client = vision.ImageAnnotatorClient()
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    if texts:
        return texts[0].description.strip()
    return ""
