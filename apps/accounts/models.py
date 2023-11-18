from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class Org(AbstractUser):
    username = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        error_messages={"unique": "Orginization with this name already exists"},
        verbose_name="org name",
    )

    first_name = None
    last_name = None

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "Org"
        verbose_name_plural = "Orgs"


class OrgLocation(models.Model):
    org = models.OneToOneField(Org, on_delete=models.CASCADE, null=True, blank=True)
    country = models.CharField(unique=False, max_length=50)
    region = models.CharField(unique=False, max_length=50)
    zip = models.IntegerField(unique=False)
    city = models.CharField(unique=False, max_length=50)
    street_address = models.CharField(unique=False, max_length=50)

    class Meta:
        verbose_name = "OrgLocationInfo"
        verbose_name_plural = "OrgsLocationInfo"


class OrgContactInfo(models.Model):
    org = models.OneToOneField(Org, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.PositiveIntegerField(unique=False)
    email = models.EmailField(unique=False)

    class Meta:
        verbose_name = "OrgContactInfo"
        verbose_name_plural = "OrgsContactInfo"


class OrgInfo(models.Model):
    org = models.OneToOneField(Org, on_delete=models.CASCADE, null=True, blank=True)
    desc = models.TextField(max_length=1000, unique=False)
    website = models.URLField(unique=False)

    class Meta:
        verbose_name = "OrgInfo"
        verbose_name_plural = "OrgsInfo"


class Item(models.Model):  # model for all items
    item_name = models.CharField(max_length=100, unique=False, primary_key=False)
    org = models.ForeignKey("org", on_delete=models.CASCADE, blank=True)
    want = models.BooleanField(unique=False, max_length=100, default=True)
    count = models.SmallIntegerField(unique=False, default=1)

    def __str__(self) -> str:
        return self.item_name

    class Meta:
        unique_together = "org", "item_name"
        verbose_name = "Item"
        verbose_name_plural = "Items"
