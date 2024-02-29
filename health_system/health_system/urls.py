"""
URL configuration for health_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include("dashboard_app.urls")),
    path("administrator/", include("administration_app.urls")),
    path("nurse/", include("nurse_app.urls")),
    path("doctor/", include("doctor_app.urls")),
    path("patient/", include("patient_app.urls")),
    # path("api/doctors/", include("doctor_app.urls")),
    # path("api/nurses/", include("nurse_app.urls")),
    # path("api/patients/", include("patient_app.urls")),
    path("insurance/", include("insurance_app.urls")),
]
