from django.test import TestCase
from apps.items.models import Item
from apps.accounts.models import Org


class ItemTestCases(TestCase):
    def setUp(self):
        org = Org.objects.create(username="Org")
        Item.objects.create(item_name="Item", org=org)

    def test_str_method(self):
        # makes sure the str_method returns the right str
        expected_result = "Item"
        result = str(Item.objects.get(item_name="Item"))
        self.assertEqual(result, expected_result)
