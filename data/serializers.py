# myapp/serializers.py
from rest_framework import serializers
from .models import News, Art


class FeedbackSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField()
