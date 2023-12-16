from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
