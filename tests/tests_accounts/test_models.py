from django.test import TestCase
from apps.accounts.models import Org, OrgLocation, OrgContactInfo, OrgInfo


MAX_ORG_LOCATION_FIELD_LENGTH = 50
MAX_USERNAME_LENGTH = 100


class OrgTestCases(TestCase):
    def setUp(self):
        Org.objects.create(username="MyOrg")

    def test_get_absolute_url_method(self):
        # makes sure the absolute url function returns the expected URL
        test_org = Org.objects.get(username="MyOrg")
        expected_output = "/nonprofits/homepage/MyOrg/"
        self.assertEqual(test_org.get_absolute_url(), expected_output)


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

    def test_str_method(self):
        # tests the __str__ method of the OrgLocation class
        test_org = Org.objects.get(username="MyOrg")
        test_org_location = OrgLocation.objects.get(org=test_org)
        expected_result = "MyOrg"
        self.assertEqual(str(test_org_location), expected_result)


class OrgContactInfoTestCases(TestCase):
    def setUp(self):
        test_org = Org.objects.create(username="MyOrg")
        OrgContactInfo.objects.create(
            org=test_org, phone=123456789, email="MyAwesomeEmail@gmail.com"
        )

    def test_str_method(self):
        expected_result = "MyOrg"
        org = Org.objects.get(username="MyOrg")
        test_org_contact_info = OrgContactInfo.objects.get(org=org)
        self.assertEqual(str(test_org_contact_info), expected_result)


class OrgInfoTestCases(TestCase):
    def setUp(self):
        test_org = Org.objects.create(username="MyOrg")
        OrgInfo.objects.create(
            org=test_org, desc="My amazing description", website="https://google.com"
        )

    def test_str_method(self):
        expected_result = "MyOrg"
        org = Org.objects.get(username="MyOrg")
        test_org_contact_info = OrgInfo.objects.get(org=org)
        self.assertEqual(str(test_org_contact_info), expected_result)
