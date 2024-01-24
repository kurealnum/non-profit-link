from django.test import TestCase, Client
from django.urls import reverse
from apps.items.models import Item
from apps.accounts.models import Org, OrgLocation


class IndexTest(TestCase):
    def setUp(self) -> None:
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

    # yes, these two methods should proably return model instances
    def test_items_return(self):
        # tests that the 'top_5_items' key in the context returns the correct stuff
        response = self.client.get(self.url)
        expected_response = [[str, int, int]] * 5
        self.assertIn("top_5_items", response.context)

        context = response.context["top_5_items"]
        expected_length = 5
        types = [[type(j) for j in i] for i in context]
        self.assertEqual(types, expected_response)
        self.assertEqual(len(context), expected_length)

    def test_orgs_return(self):
        # tests that the 'random_5_orgs' key in the context returns the correct stuff
        response = self.client.get(self.url)
        expected_response = [[str, str, str]] * 5
        self.assertIn("random_5_orgs", response.context)

        context = response.context["random_5_orgs"]
        expected_length = 5
        types = [[type(j) for j in i] for i in context]
        self.assertEqual(types, expected_response)
        self.assertEqual(len(context), expected_length)
