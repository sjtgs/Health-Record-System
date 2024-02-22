from django.contrib.auth.models import User, Group
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
        return f"{self.towns}"


# Hospital Administration Information
class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    # Basic Administrator Information
    auto_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nrc = models.CharField(max_length=255)

    # Address Information
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    provinces = models.ForeignKey(Province, on_delete=models.CASCADE)
    towns = models.ForeignKey(Town, on_delete=models.CASCADE)
    address = models.TextField()

    # Contact Information
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

    def save(self, *args, **kwargs):
        # Check if the User - Administator exist, if not create a new one
        if not self.user:
            username = (self.first_name[:2] + self.last_name[:2] + self.nrc[:4]).lower()
            password = username

            #  Create a Administrator username
            self.user = User.objects.create_user(username=username, password=password)

        if not self.group:
            # Get or create Administrator group
            administrator_group, _ = Group.objects.get_or_create(name="Administrator")
            self.group = administrator_group

        super().save(*args, **kwargs)
        administrator_group, _ = Group.objects.get_or_create(name="Administrator")
        self.user.groups.add(administrator_group)
        self.user.save()


# Administrator Image
class AdministratorImage(models.Model):
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="Images/Medical_Stuff_Images/Administrator_Images/"
    )
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Image for {self.administrator.first_name}{self.administrator.last_name}"
        )
