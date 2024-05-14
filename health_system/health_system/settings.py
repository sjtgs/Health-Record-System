"""
Django settings for health_system project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os


from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# LOG_DIR = os.path.join(BASE_DIR, "logs")

# if not os.path.exists(LOG_DIR):
#     os.makedirs(LOG_DIR)


# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "formate": "{levelname} {asctime} {module} {message}",
#             "style": "{",
#         },
#     },
#     "handlers": {
#         "doctor_logfile": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": os.path.join(LOG_DIR, "logs/doctor.log"),
#             "formatter": "verbose",
#         },
#         "patient_logfile": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": os.path.join(LOG_DIR, "logs/patient.log"),
#             "formatter": "verbose",
#         },
#         "nurse_logfile": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": os.path.join(LOG_DIR, "logs/nurse.log"),
#             "formatter": "verbose",
#         },
#         "administrations_logfile": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": os.path.join(LOG_DIR, "logs/administrations.log"),
#             "formatter": "verbose",
#         },
#         "pharmacy_logfile": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": os.path.join(LOG_DIR, "logs/pharmacy.log"),
#             "formatter": "verbose",
#         },
#         "insurance_logfile": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": os.path.join(LOG_DIR, "logs/insurance.log"),
#             "formatter": "verbose",
#         },
#     },
#     "logger": {
#         "doctor": {
#             "handlers": ["doctor_logfile"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#         "patient": {
#             "handlers": ["patient_logfile"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#         "nurse": {
#             "handlers": ["nurse_logfile"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#         "administration": {
#             "handlers": ["administrations_logfile"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#         "pharmacy": {
#             "handlers": ["pharmacy_logfile"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#         "insurance": {
#             "handlers": ["insurance_logfile"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#     },
# }

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "SECRET KEY"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Celery Configuration
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "administration_app",
    "patient_app",
    "doctor_app",
    "dashboard_app",
    "insurance_app",
    "nurse_app",
    "rest_framework",
    # "channels",
    "crispy_forms",
    "bootstrap4",
    "crispy_bootstrap4",
]

CRISPY_TEMPLATE_PACK = "uni_form"
CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"


# ASGI_APPLICATION = 'health_system.routing.application'


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "health_system.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "dashboard_app/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "health_system.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
