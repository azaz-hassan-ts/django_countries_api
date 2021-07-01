from django.db.models import fields
from rest_framework import serializers
from countries import models
from countries.models import Countries

class CountriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields = ('id', 'name', 'capital')