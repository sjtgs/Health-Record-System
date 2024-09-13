import logging

# Pharmacy Logger
logger = logging.getLogger("pharmacy_app")
logger.setLevel(logging.INFO)

# Create Pharmacy Logger File handler
log_file = "logs/phamarcy_creation.log"
file_handler = logging.FileHandler(log_file)


# Create formatter and set it to handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add file handler to logger 
logger.addHandler(file_handler)

# Pharmcay Logger Function 
def log_pharmacy_creation(pharmacy_instance):
    if hasattr(logger, "info"):
        logger.info(
            f"Pharmacy Created " {pharmacy_instance}
        )
    else:
        if hasattr(logger, "error"):
            logger.error(
                "Error Pharmacy : Logger object doesn't have an 'info' attribute."
            ) 
