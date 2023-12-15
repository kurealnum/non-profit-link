from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    input_id = serializers.IntegerField()

    class Meta:
        model = Item
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Item.objects.all(),
                fields=["org", "item_name"],
                message="Duplicate items!",
            )
        ]

    # identifying which input to send an error to on the frontend
    # TODO: figure out how to make this work
