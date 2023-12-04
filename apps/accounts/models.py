from django.contrib.auth.models import AbstractUser
from django.db import models

# for more info on models, see the database diagram in diagrams/


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

    def get_absolute_url(self):
        return f"/nonprofits/homepage/{self.username}/"

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

    def __str__(self):
        return str(self.org)

    class Meta:
        verbose_name = "OrgLocationInfo"
        verbose_name_plural = "OrgsLocationInfo"


class OrgContactInfo(models.Model):
    org = models.OneToOneField(Org, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.PositiveIntegerField(unique=False)
    email = models.EmailField(unique=False)

    def __str__(self):
        return str(self.org)

    class Meta:
        verbose_name = "OrgContactInfo"
        verbose_name_plural = "OrgsContactInfo"


class OrgInfo(models.Model):
    org = models.OneToOneField(Org, on_delete=models.CASCADE, null=True, blank=True)
    desc = models.TextField(max_length=1000, unique=False)
    website = models.URLField(unique=False)

    def __str__(self):
        return str(self.org)

    class Meta:
        verbose_name = "OrgInfo"
        verbose_name_plural = "OrgsInfo"
