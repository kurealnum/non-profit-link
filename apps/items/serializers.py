from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    # ????
    input_id = serializers.IntegerField()

    class Meta:
        model = Item
        fields = "__all__"
        extra_kwargs = {"input_id": {"error_messages"}}
        validators = [
            UniqueTogetherValidator(
                queryset=Item.objects.all(),
                fields=["org", "item_name"],
                message="You cannot have duplicate items!",
            )
        ]
