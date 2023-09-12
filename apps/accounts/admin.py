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
                    "email",
                ]
            },
        )
    ]
    username = None
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = org
    list_display = [
        "email",
    ]
    ordering = ("-email",)


admin.site.register(org, CustomUserAdmin)
