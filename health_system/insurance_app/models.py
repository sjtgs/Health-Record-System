from django.db import models
from administration_app.models import Country, Province, Town


class InsuranceCompany(models.Model):
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    provinces = models.ForeignKey(Province, on_delete=models.CASCADE)
    towns = models.ForeignKey(Town, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField()
    contact_number = models.PositiveIntegerField()
    email = models.EmailField()
    website = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
