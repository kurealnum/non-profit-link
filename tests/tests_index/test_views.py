from django.test import TestCase, Client
from django.urls import reverse
from apps.items.models import Item
from apps.accounts.models import Org, OrgLocation


class IndexTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("index")

        # create a few orgs to test
        for i in range(6):
            instance = Org.objects.create(username=f"Org{i}")
            Item.objects.create(item_name=f"Item{i}", org=instance)
            OrgLocation.objects.create(
                org=instance,
                region=f"region{i}",
                city=f"city{i}",
                country=f"country{i}",
                zip=1 + 1,
                street_address=f"street{i}",
            )
