from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Org, OrgContactInfo, OrgInfo, OrgLocation, Item


@admin.register(Org)
class OrgAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "non_profit_name",
                ]
            },
        )
    ]
    username = None
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Org
    list_display = [
        "non_profit_name",
    ]
    ordering = ("-non_profit_name",)


@admin.register(OrgContactInfo)
class OrgContactInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OrgInfo)
class OrgInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OrgLocation)
class OrgLocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class OrgItemAdmin(admin.ModelAdmin):
    pass
