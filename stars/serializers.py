from rest_framework import serializers
from .models import Star

class StarSerializer(serializers.ModelSerializer):
    star = serializers.PrimaryKeyRelatedField(many=True, queryset=Star.objects.all())

    class Meta:
        model = Star
        field = ['id', 'title', 'slug', 'content', 'photo', 'time_create', 'time_update', 'is_published', 'cat',]
