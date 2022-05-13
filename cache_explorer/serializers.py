from rest_framework import serializers
from .models import Cache


class CacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cache
        fields = "__all__"
