# serializers.py
from rest_framework import serializers
from .models import WebcamVideo

class WebcamVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebcamVideo
        fields = '__all__'