from django.test import TestCase, Client
from django.urls import reverse
from apps.items.models import Item
from apps.accounts.models import Org, OrgLocation, OrgInfo, OrgContactInfo
from apps.items.views import search_items_results


class SearchItemResultsTests(TestCase):
    def setUp(self):
        self.url = reverse("search_items_results")
        self.client = Client()
        instance1 = Org.objects.create(username="MyOrg1")
        Item.objects.create(org=instance1, item_name="MyWantedItem", want=True)

    def test_valid_response_status(self):
        # tests that the response status is correct
        response = self.client.get(self.url)
        expected_result = 200
        result = response.status_code
        self.assertEqual(result, expected_result)

    # This sections is testing every possible input to this view. Just look at the data= field in each function for more info.
    def test_context_content_with_parameters_1(self):
        # check if the content of the context is correct with these paramters
        response = self.client.get(
            self.url,
            data={
                "search": "MyWantedItem",
                "org": "item",
                "is_want": "on",
                "is_need": "on",
            },
        )
        context = response.context
        self.assertEqual(context["all_items"][0].__class__, Item)
        self.assertEqual(context["search"], "MyWantedItem")
        self.assertEqual(context["org"], "item")

    def test_context_content_with_parameters_2(self):
        # check if the content of the context is correct with these paramters
        response = self.client.get(
            self.url,
            data={
                "search": "MyOrg1",
                "org": "org",
                "is_want": "on",
                "is_need": "on",
            },
        )
        context = response.context
        self.assertEqual(context["all_items"][0].__class__, Item)
        self.assertEqual(context["search"], "MyOrg1")
        self.assertEqual(context["org"], "org")

    def test_context_content_with_parameters_3(self):
        # check if the content of the context is correctthese paramters
        response = self.client.get(
            self.url,
            data={
                "search": "MyWantedItem",
                "org": "item",
                "is_want": "on",
                "is_need": "",
            },
        )
        context = response.context
        self.assertEqual(len(context["all_items"]), 0)
        self.assertEqual(context["search"], "MyWantedItem")
        self.assertEqual(context["org"], "item")

    def test_context_content_with_parameters_4(self):
        # check if the content of the context is correctthese paramters
        response = self.client.get(
            self.url,
            data={
                "search": "MyWantedItem",
                "org": "item",
                "is_want": "",
                "is_need": "on",
            },
        )
        context = response.context
        self.assertEqual(len(context["all_items"]), 1)
        self.assertEqual(context["search"], "MyWantedItem")
        self.assertEqual(context["org"], "item")

    def test_context_content_with_parameters_5(self):
        # check if the content of the context is correctthese paramters
        response = self.client.get(
            self.url,
            data={
                "search": "MyWantedItem",
                "org": "item",
                "is_want": "",
                "is_need": "",
            },
        )
        context = response.context
        self.assertEqual(len(context["all_items"]), 1)
        self.assertEqual(context["search"], "MyWantedItem")
        self.assertEqual(context["org"], "item")

    def test_context_content_with_parameters_6(self):
        # check if the content of the context is correctthese paramters
        response = self.client.get(
            self.url,
            data={
                "search": "MyOrg1",
                "org": "org",
                "is_want": "on",
                "is_need": "",
            },
        )
        context = response.context
        self.assertEqual(len(context["all_items"]), 0)
        self.assertEqual(context["search"], "MyOrg1")
        self.assertEqual(context["org"], "org")

    def test_context_content_with_parameters_7(self):
        # check if the content of the context is correctthese paramters
        response = self.client.get(
            self.url,
            data={
                "search": "MyOrg1",
                "org": "org",
                "is_want": "",
                "is_need": "on",
            },
        )
        context = response.context
        self.assertEqual(len(context["all_items"]), 1)
        self.assertEqual(context["search"], "MyOrg1")
        self.assertEqual(context["org"], "org")

    def test_context_content_with_parameters_8(self):
        # check if the content of the context is correctthese paramters
        response = self.client.get(
            self.url,
            data={
                "search": "MyOrg1",
                "org": "org",
                "is_want": "",
                "is_need": "",
            },
        )
        context = response.context
        self.assertEqual(len(context["all_items"]), 1)
        self.assertEqual(context["search"], "MyOrg1")
        self.assertEqual(context["org"], "org")
