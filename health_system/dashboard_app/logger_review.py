import logging

# Configure logger
logger = logging.getLogger("dashboard_app")
logger.setLevel(logging.INFO)

# Create file handler
log_file = "logs/patient_review_appointment.log"
file_handler = logging.FileHandler(log_file)

# Create formatter and set it to handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add file handler to logger
logger.addHandler(file_handler)


# Define logging functions - Patient Review Appointment
def log_patient_review_appointment(review_instance):
    if hasattr(logger, "info"):
        logger.info(
            f"Patient Review Appointment Created : Patient: {review_instance.patient}, Doctor: {review_instance.doctor}, Nurse: {review_instance.nurse}, Appointment Date: {review_instance.appointment_date},  ID: {review_instance.appointment_id}"
        )
    else:
        if hasattr(logger, "error"):
            logger.error(
                "Error Patient Review Appointment: Logger object doesn't have an 'info' attribute."
            )
