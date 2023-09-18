from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class OrgLocation(models.Model):
    org = models.ForeignKey("org", on_delete=models.CASCADE, related_name="+")
    country = models.CharField(unique=False, max_length=50)
    region = models.CharField(unique=False, max_length=50)
    zip = models.SmallIntegerField(unique=False, null=False)  # can be null
    city = models.CharField(unique=False, max_length=50)
    street_address = models.CharField(unique=True, max_length=50)

    class Meta:
        verbose_name = "OrgLocationInfo"
        verbose_name_plural = "OrgsLocationInfo"


class OrgContactInfo(models.Model):
    org = models.ForeignKey("org", on_delete=models.CASCADE, related_name="+")
    phone = models.PositiveIntegerField(unique=True)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "OrgContactInfo"
        verbose_name_plural = "OrgsContactInfo"


class OrgInfo(models.Model):
    org = models.ForeignKey("org", on_delete=models.CASCADE, related_name="+")
    desc = models.CharField(max_length=1000, unique=False)
    website = models.URLField(unique=False)

    class Meta:
        verbose_name = "OrgInfo"
        verbose_name_plural = "OrgsInfo"


class Org(AbstractUser):
    objects: CustomUserManager = CustomUserManager()

    org_name = models.CharField(
        unique=False, max_length=100, default="UN-NAMED-ORG", null=False
    )
    # loc = models.OneToOneField(OrgLocation, on_delete=models.CASCADE, null=True)
    # contact = models.OneToOneField(OrgContactInfo, on_delete=models.CASCADE, null=True)
    # info = models.OneToOneField(OrgInfo, on_delete=models.CASCADE, null=True)
    username = None
    USERNAME_FIELD = "org_name"
    REQUIRED_FIELDS = ()  # type: ignore

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "Org"
        verbose_name_plural = "Orgs"


class Item(models.Model):  # model for all items
    org = models.ForeignKey("org", on_delete=models.CASCADE)
    want = models.BooleanField(unique=False, max_length=100, default=True)
    count = models.SmallIntegerField(unique=False, default=1)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
