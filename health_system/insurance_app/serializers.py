from rest_framework import serializers
from .models import InusranceCompany


class InsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InusranceCompany
        fields = "__all__"
