from django.test import TestCase, Client
from django.urls import reverse
from django.db.models.query import QuerySet
from apps.items.models import Item
from apps.items.models import Org


class IndexTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("index")

        # create a few orgs to test
        for i in range(6):
            instance = Org.objects.create(username=f"Org{i}")
            Item.objects.create(item_name=f"Item{i}", org=instance)

    # yes, these two methods should proably return model instances
    def test_items_return(self):
        # tests that the 'top_5_items' key in the context returns the correct stuff
        response = self.client.get(self.url)
        expected_response = [str] * 5
        expected_length = 5
        context = response.context["top_5_items"]
        types = [type(i[0]) for i in context]
        self.assertEqual(types, expected_response)
        self.assertEqual(len(context), expected_length)

    def test_orgs_return(self):
        # tests that the 'random_5_orgs' key in the context returns the correct stuff
        response = self.client.get(self.url)
        expected_response = [str] * 5
        expected_length = 5
        context = response.context["random_5_orgs"]
        types = [type(i[0]) for i in context]
        self.assertEqual(types, expected_response)
        self.assertEqual(len(context), expected_length)
