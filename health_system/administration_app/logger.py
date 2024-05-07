import logging

# Configure logger
logger = logging.getLogger("administration_app")
logger.setLevel(logging.INFO)

# Create file handler
log_file = "logs/users_creation.log"
file_handler = logging.FileHandler(log_file)

# Create formatter and set it to handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add file handler to logger
logger.addHandler(file_handler)


# Define logging functions - Administrator, Doctor, Nurse , Patient
def log_administrator_creation(administration_instance):
    if hasattr(logger, "info"):
        logger.info(
            f"Administrator Created : First Name: {administration_instance.first_name}, Last Name: {administration_instance.last_name}, Gender: {administration_instance.gender}, NRC: {administration_instance.nrc},  ID: {administration_instance.auto_id}"
        )
    else:
        if hasattr(logger, "error"):
            logger.error(
                "Error Administrator: Logger object doesn't have an 'info' attribute."
            )


def log_doctor_creation(doctor_instance):
    if hasattr(logger, "info"):
        logger.info(
            f"Doctor Created: First Name: {doctor_instance.first_name},  Last Name: {doctor_instance.last_name}, Gender: {doctor_instance.gender}, NRC: {doctor_instance.nrc}, ID: {doctor_instance.auto_id}"
        )

    else:
        if hasattr(logger, "error"):
            logger.error(
                "Error Doctor: Logger object doesn't have an 'info' attribute."
            )


def log_nurse_creation(nurse_instance):
    if hasattr(logger, "info"):
        logger.info(
            f"Nurse Created: First Name: {nurse_instance.first_name}, Last Name: {nurse_instance.last_name}, Gender: {nurse_instance.gender}, NRC: {nurse_instance.nrc},  ID: {nurse_instance.auto_id}"
        )
    else:
        if hasattr(logger, "error"):
            logger.error("Error Nurse: Logger object doesn't have an 'info' attribute.")


def log_patient_creation(patient_instance):
    if hasattr(logger, "info"):
        logger.info(
            f"Patient Created : First Name: {patient_instance.first_name}, Last Name: {patient_instance.last_name}, Gender: {patient_instance.gender}, NRC: {patient_instance.nrc},  ID : {patient_instance.auto_id}"
        )
    else:
        if hasattr(logger, "error"):
            logger.error(
                "Error Patient: Logger object doesn't have an 'info' attribute."
            )
