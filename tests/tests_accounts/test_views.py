from django.test import TestCase, Client
from django.urls import reverse
from apps.accounts.models import Org


class EditOrgInfoTest(TestCase):
    def setUp(self):
        # this client will be logged in. if you want a logged out client, remake it with Client()
        self.client = Client()
        user = Org.objects.create(username="MyOrg")
        user.set_password("THISismyAMAZINGPa$$sword")
        user.save()
        print(self.client.login(username="MyOrg", password="THISismyAMAZINGPa$$sword"))

    def test_method_request_type(self):
        # tests to make sure the method only accepts PUT requests
        response = self.client.get(reverse("edit_org_info"))
        expected_response = 405
        self.assertEqual(response.status_code, expected_response)
