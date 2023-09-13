from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import org, org_contact_info, org_info, org_loc, item


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
    model = admin.ModelAdmin
    list_display = [
        "non_profit_name",
    ]
    ordering = ("-non_profit_name",)
    pass


admin.site.register(org, OrgAdmin)
