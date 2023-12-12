from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        extra_kwargs = {
            "non_field_errors": {
                "error_messages": {
                    "unique": "There exists an item with this name already!"
                }
            }
        }
