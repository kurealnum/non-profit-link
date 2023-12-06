from django.forms import ModelForm

from .models import Item


class CustomItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["item_name", "units_description", "count"]
