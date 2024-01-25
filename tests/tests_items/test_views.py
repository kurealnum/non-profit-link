from rest_framework.test import APIClient, APITestCase
from django.test import TestCase, Client
from django.urls import reverse
from apps.items.models import Item
from apps.accounts.models import Org


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


class SearchItemsTests(TestCase):
    def setUp(self):
        self.url = reverse("search_items")
        instance = Org.objects.create(username="MyOrg")
        Item.objects.create(item_name="MyItem", want=True, org=instance)
        Item.objects.create(item_name="MyItem2", want=False, org=instance)

    def test_context_content(self):
        # tests that the context is correct (in this case it should be a queryset with length 2)
        response = self.client.get(self.url)
        expected_result = [Item, Item]
        result = [i.__class__ for i in response.context["all_items"]]
        self.assertEqual(result, expected_result)


class RequestDataAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("manage_item")
        self.user = Org.objects.create(username="MyOrg")
        self.user.set_password("THISismyAMAZINGPa$$sword")
        self.user.save()
        self.client.login(username="MyOrg", password="THISismyAMAZINGPa$$sword")

        # default item
        Item.objects.create(org=self.user, item_name="MyItem")

    def test_post_content_context_with_no_errors(self):
        # tests the output of the post method when the input is valid
        response = self.client.post(
            self.url,
            data={
                "item_name": "MyAwesomeItem",
                "want": True,
                "units_description": "units",
                "count": 3,
                "org": self.user,
            },
        )
        expected_status = 201
        status = response.status_code
        self.assertEqual(expected_status, status)

    def test_post_content_context_with_errors(self):
        # tests the output of the post method when the input is not valid
        response = self.client.post(
            self.url,
            data={
                "item_name": "MyItem",
                "want": True,
                "units_description": "units",
                "count": 3,
                "org": self.user,
                "input_id": 1,  # this is for frontend stuff
            },
        )
        expected_status = 400
        status = response.status_code
        context = response.json()
        self.assertEqual(expected_status, status)
        self.assertTrue("errors" in context)
        self.assertTrue("input_id" in context)

    def test_put_content_context_with_no_errors(self):
        # tests the output of the put method when the input is valid
        Item.objects.create(org=self.user, item_name="WhoKnows")
        response = self.client.put(
            self.url,
            {
                "old_item_name": "WhoKnows",
                "new_item_name": "WhoKnowsNew",
                "want": True,
                "units_description": "boxes",
                "org": self.user,
                "count": 3,
                "input_id": 1,  # this is for frontend stuff
            },
            format="multipart",
        )
        expected_status = 200
        status = response.status_code
        self.assertEqual(status, expected_status)

    def test_put_content_context_with_errors_1(self):
        # tests the output of the put method when the input is invalid
        Item.objects.create(org=self.user, item_name="TestItem1")
        response = self.client.put(
            self.url,
            {
                "old_item_name": "TestItem1",
                "new_item_name": "TestItem1",
                "want": True,
                "units_description": "boxes",
                "org": self.user,
                "count": 3,
                "input_id": 1,  # this is for frontend stuff
            },
            format="multipart",
        )
        expected_status = 400
        status = response.status_code
        self.assertEqual(status, expected_status)

    def test_put_content_context_with_errors_2(self):
        # tests the output of the put method when the input is invalid
        response = self.client.put(
            self.url,
            {
                "old_item_name": "ThisDoesNotExist",
                "new_item_name": "TestItem1",
                "want": True,
                "units_description": "boxes",
                "org": self.user,
                "count": 3,
                "input_id": 1,  # this is for frontend stuff
            },
            format="multipart",
        )
        expected_status = 404
        status = response.status_code
        self.assertEqual(status, expected_status)


class UrlDataAPIViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Org.objects.create(username="MyOrg")
        self.user.set_password("MyAwesomePassword")
        self.user.save()
        self.client.login(username="MyOrg", password="MyAwesomePassword")

    def test_get_with_no_errors(self):
        # tests the get method when everything is valid
        Item.objects.create(org=self.user, item_name="MyItem")
        url = reverse("manage_item_with_name", args=("MyItem",))
        response = self.client.get(url)
        expected_status = 200
        status = response.status_code
        self.assertEqual(status, expected_status)

    def test_get_with_errors(self):
        # tests the get method with invalid name
        url = reverse("manage_item_with_name", args=("IDon'tExist",))
        response = self.client.get(url)
        expected_status = 404
        status = response.status_code
        self.assertEqual(status, expected_status)

    def test_delete_with_no_errors(self):
        Item.objects.create(org=self.user, item_name="Item")
        url = reverse("manage_item_with_name", args=("Item",))
        response = self.client.delete(url)
        expected_status = 204
        status = response.status_code
        self.assertEqual(status, expected_status)

    def test_delete_with_errors(self):
        url = reverse("manage_item_with_name", args=("IstillDon'tExist",))
        response = self.client.get(url)
        expected_status = 404
        status = response.status_code
        self.assertEqual(status, expected_status)
