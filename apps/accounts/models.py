from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class OrgLocation(models.Model):
    country = models.CharField(unique=False, max_length=50)
    region = models.CharField(unique=False, max_length=50)
    zip = models.SmallIntegerField(unique=False, null=False)  # can be null
    city = models.CharField(unique=False, max_length=50)
    street_address = models.CharField(unique=True, max_length=50)


class OrgContactInfo(models.Model):
    phone = models.PositiveIntegerField(unique=True)
    email = models.EmailField(unique=True)


class OrgInfo(models.Model):
    desc = models.CharField(max_length=1000, unique=False)
    website = models.URLField(unique=False)


class Org(AbstractUser):
    objects: CustomUserManager = CustomUserManager()

    non_profit_name = models.CharField(
        unique=True, max_length=100, default="Un-named non-profit :(", null=False
    )
    loc = models.OneToOneField(OrgLocation, on_delete=models.CASCADE, null=True)
    contact = models.OneToOneField(OrgContactInfo, on_delete=models.CASCADE, null=True)
    info = models.OneToOneField(OrgInfo, on_delete=models.CASCADE, null=True)
    username = None
    USERNAME_FIELD = "non_profit_name"
    REQUIRED_FIELDS = ()  # type: ignore

    def __str__(self) -> str:
        return self.email


class Item(models.Model):  # model for all items
    org = models.ForeignKey("org", on_delete=models.CASCADE)
    want = models.BooleanField(unique=False, max_length=100, default=True)
    count = models.SmallIntegerField(unique=False, default=1)
