from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *
import django_filters

class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        #fields = ('name')

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        #fields = ('temperature', 'humidity',)