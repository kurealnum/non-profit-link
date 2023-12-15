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
    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)

        if self.errors:
            for field, errors in self.errors.items():
                for error in errors:
                    error_dict = {"error": error, "input_id": data.get("input_id")}
                    self.errors[field].append(error_dict)

        return internal_value
