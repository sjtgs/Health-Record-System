from django.db import models
from administration_app.models import Country, Province, Town


# Created Pharmacy Model
class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    location = models.PointField()
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"
