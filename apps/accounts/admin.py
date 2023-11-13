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


class OrgAdmin(UserAdmin):
    inlines = [OrgContactInfoInline, OrgInfoInline, OrgLocationInline, ItemInline]
    fields = ["username", "password"]
    fieldsets = []


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


admin.site.register(Org, OrgAdmin)
