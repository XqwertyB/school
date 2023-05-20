# myapp/serializers.py
from rest_framework import serializers
from .models import News, Art


class FeedbackSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    number = serializers.CharField(max_length=13)
    message = serializers.CharField()


class NewsList(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class ArtList(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = "__all__"