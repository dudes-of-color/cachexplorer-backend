from rest_framework import serializers
from .models import CacheExplorer


class CacheExplorerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CacheExplorer
        fields = "__all__"
