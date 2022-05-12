from rest_framework import serializers
from .models import CookieStand


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookieStand
        fields = "__all__"
