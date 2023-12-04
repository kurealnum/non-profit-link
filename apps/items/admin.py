from django.contrib import admin
from .models import Item


# Register your models here.
@admin.register(Item)
class OrgItemAdmin(admin.ModelAdmin):
    list_display = ["item_name", "count", "org"]
