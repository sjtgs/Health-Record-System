from django.contrib import admin
from administration_app.models import Administrator, AdministratorImage


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = (
        "auto_id",
        "user",
        "first_name",
        "last_name",
        "date_of_birth",
        "gender",
        "nrc",
        "countries",
        "provinces",
        "towns",
        "address",
        "email",
        "phone_number",
        "created_at",
        "updated_at",
    )
    search_fields = ("first_name", "last_name", "nrc", "email", "phone_number")
    list_filter = (
        "gender",
        "countries",
        "provinces",
        "towns",
        "created_at",
        "updated_at",
    )


@admin.register(AdministratorImage)
class AdministratorImageAdmin(admin.ModelAdmin):
    list_display = ("administrator", "image", "description", "uploaded_at")
    search_fields = ("administrator__first_name", "doctor__last_name", "description")
    list_filter = ("uploaded_at",)
