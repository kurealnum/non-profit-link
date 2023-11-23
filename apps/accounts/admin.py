from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Item, Org, OrgContactInfo, OrgInfo, OrgLocation


# inlines for Org
class OrgContactInfoInline(admin.TabularInline):
    model = OrgContactInfo


class OrgInfoInline(admin.TabularInline):
    model = OrgInfo


class OrgLocationInline(admin.TabularInline):
    model = OrgLocation


class ItemInline(admin.TabularInline):
    model = Item


# registering models
@admin.register(Org)
class OrgAdmin(UserAdmin):
    inlines = [OrgContactInfoInline, OrgInfoInline, OrgLocationInline, ItemInline]
    fields = ["username", "password"]
    list_display = ["username", "email", "is_staff"]
    fieldsets = []


@admin.register(OrgContactInfo)
class OrgContactInfoAdmin(admin.ModelAdmin):
    list_display = ["org", "phone", "email"]


@admin.register(OrgInfo)
class OrgInfoAdmin(admin.ModelAdmin):
    list_display = ["org", "website"]


@admin.register(OrgLocation)
class OrgLocationAdmin(admin.ModelAdmin):
    list_display = ["org", "country", "region", "zip", "city", "street_address"]


@admin.register(Item)
class OrgItemAdmin(admin.ModelAdmin):
    list_display = ["item_name", "count", "org"]
