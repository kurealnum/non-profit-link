from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class org_loc(models.Model):
    country = models.CharField(unique=False, max_length=50)
    region = models.CharField(unique=False, max_length=50)
    zip = models.SmallIntegerField(unique=False, null=False)  # can be null
    city = models.CharField(unique=False, max_length=50)
    street_address = models.CharField(unique=True, max_length=50)


class org_contact_info(models.Model):
    phone = models.PositiveIntegerField(unique=True)  # max_length for 11234567890
    email = models.EmailField(unique=True)


class org_info(models.Model):
    desc = models.CharField(max_length=1000, unique=False)
    website = models.URLField(unique=False)


class org(AbstractUser):
    objects: CustomUserManager = CustomUserManager()

    non_profit_name = models.CharField(
        unique=True, max_length=100, default="Un-named non-profit :("
    )
    loc = models.OneToOneField(org_loc, on_delete=models.CASCADE)
    contact = models.OneToOneField(org_contact_info, on_delete=models.CASCADE)
    info = models.OneToOneField(org_info, on_delete=models.CASCADE)

    USERNAME_FIELD = "non_profit_name"
    REQUIRED_FIELDS = ()  # type: ignore

    def __str__(self) -> str:
        return self.email


class item(models.Model):  # model for all items
    org = models.ForeignKey(org, on_delete=models.CASCADE)
    want = models.BooleanField(unique=False, max_length=100)
    count = models.SmallIntegerField(unique=False, default=1)
