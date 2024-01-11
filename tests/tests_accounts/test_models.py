from django.db import models
from django.test import TestCase
from apps.accounts.models import Org, OrgLocation
from django.db.utils import IntegrityError


MAX_ORG_LOCATION_FIELD_LENGTH = 50
MAX_USERNAME_LENGTH = 100


class OrgTestCases(TestCase):
    def setUp(self):
        Org.objects.create(username="MyOrg")

    def test_is_absolute_url(self):
        # makes sure the absolute url function returns the expected URL
        test_org = Org.objects.get(username="MyOrg")
        expected_output = "/nonprofits/homepage/MyOrg/"
        self.assertEqual(test_org.get_absolute_url(), expected_output)

    def test_str_method(self):
        # tests if the __str__ function in Org returns the expected value
        test_org = Org.objects.get(username="MyOrg")
        expected_output = str(test_org)
        self.assertEqual(test_org.username, expected_output)


class OrgLocationTestCases(TestCase):
    def setUp(self):
        test_org = Org.objects.create(username="MyOrg")
        OrgLocation.objects.create(
            org=test_org,
            country="US",
            region="Virginia",
            zip=12345,
            city="TomorrowLand",
            street_address="Awesome Address!",
        )

    def test_str_return(self):
        # tests the __str__ method of the OrgLocation class
        test_org = Org.objects.get(username="MyOrg")
        test_org_location = OrgLocation.objects.get(org=test_org)
        expected_result = "MyOrg"
        self.assertEqual(str(test_org_location), expected_result)
