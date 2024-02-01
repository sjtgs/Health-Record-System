from django.db import models


# Created Country Model
class Country(models.Model):
    countries = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.countries}"


# Created Province Model
class Province(models.Model):
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    provinces = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.provinces}"


# Created Town models
class Town(models.Model):
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    provinces = models.ForeignKey(Province, on_delete=models.CASCADE)
    towns = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.provinces} {self.towns}"


class InusranceCompany(models.Model):
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
