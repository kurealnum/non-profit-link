from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class orgs_loc(models.Model):
    country = models.CharField(unique=False, max_length=50)
    region = models.CharField(unique=False, max_length=50)
    zip = models.SmallIntegerField(unique=False, null=False)  # can be null
    city = models.CharField(unique=False, max_length=50)
    street_address = models.CharField(unique=True, max_length=50)


class orgs(AbstractUser):
    objects = CustomUserManager()

    non_profit_name = models.CharField(
        unique=False, max_length=100, default="Un-named non-profit :("
    )
    loc = models.OneToOneField(orgs_loc, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()  # type: ignore

    def __str__(self) -> str:
        return self.email


class item(models.Model):  # model for all items
    org = models.ForeignKey(orgs, on_delete=models.CASCADE, primary_key=True)
    want = models.BooleanField(unique=False, max_length=100)
    count = models.SmallIntegerField(unique=False, default=1)
