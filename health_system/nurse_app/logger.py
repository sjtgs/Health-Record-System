import logging

# Configure logger
logger = logging.getLogger("nurse_app")
logger.setLevel(logging.INFO)

# Create file handler
log_file = "logs/patient_book_appointment.log"
file_handler = logging.FileHandler(log_file)

# Create formatter and set it to handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add file handler to logger
logger.addHandler(file_handler)


# Define logging functions - Nurse Booking Appointment
def log_patient_book_appointment(booking_instance):
    if hasattr(logger, "info"):
        logger.info(
            f"Booking Appointment Created : Patient: {booking_instance.patient}, Doctor: {booking_instance.doctor}, Nurse: {booking_instance.nurse}, Appointment Date: {booking_instance.appointment_date},  ID: {booking_instance.appointment_id}"
        )
    else:
        if hasattr(logger, "error"):
            logger.error(
                "Error Appointment: Logger object doesn't have an 'info' attribute."
            )
