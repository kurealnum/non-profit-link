from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import org


class CustomUserAdmin(UserAdmin):
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
    model = org
    list_display = [
        "non_profit_name",
    ]
    ordering = ("-non_profit_name",)


admin.site.register(org, CustomUserAdmin)
