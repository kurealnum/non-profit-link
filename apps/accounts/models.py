from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models

# for more info on models, see the database diagram in diagrams/


class Org(AbstractUser):
    username = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        error_messages={"unique": "Organization with this name already exists"},
        verbose_name="org name",
    )

    first_name = None
    last_name = None

    def __str__(self) -> str:
        return str(self.username)

    def get_absolute_url(self):
        return reverse("homepage", args=(self.username,))

    class Meta:
        verbose_name = "Org"
        verbose_name_plural = "Orgs"

    @property
    def structured_data(self):
        selfinfo = OrgInfo.objects.get(org=self.pk)
        selflocation = OrgLocation.objects.get(org=self.pk)
        selfcontactinfo = OrgContactInfo.objects.get(org=self.pk)
        data = {
            "@context": "https://schema.org/",
            "@type": "Organization",
            "url": selfinfo.website,
            "name": self.username,
            "description": selfinfo.desc,
            "email": selfcontactinfo.email,
            "telephone": selfcontactinfo.phone,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": selflocation.street_address,
                "addressLocality": selflocation.city,
                "addressCountry": selflocation.country,
                "addressRegion:": selflocation.region,
                "postalCode": selflocation.zip,
            },
        }
        return data


class OrgLocation(models.Model):
    org = models.OneToOneField(
        Org, primary_key=True, on_delete=models.CASCADE, blank=True
    )
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
    org = models.OneToOneField(
        Org, primary_key=True, on_delete=models.CASCADE, blank=True
    )
    phone = models.PositiveIntegerField(unique=False)
    email = models.EmailField(unique=False)

    def __str__(self):
        return str(self.org)

    class Meta:
        verbose_name = "OrgContactInfo"
        verbose_name_plural = "OrgsContactInfo"


class OrgInfo(models.Model):
    org = models.OneToOneField(
        Org, primary_key=True, on_delete=models.CASCADE, blank=True
    )
    desc = models.TextField(max_length=1000, unique=False)
    website = models.URLField(unique=False)

    def __str__(self):
        return str(self.org)

    class Meta:
        verbose_name = "OrgInfo"
        verbose_name_plural = "OrgsInfo"
