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

    def test_uniqueness(self):
        # tests if the model's username argument is set to unique
        with self.assertRaises(IntegrityError):
            Org.objects.create(username="MyOrg")

    def test_max_length(self):
        # tests the maximum length of username
        expected_output = MAX_USERNAME_LENGTH
        max_length = Org._meta.get_field("username").max_length
        self.assertEqual(max_length, expected_output)

    def test_is_null(self):
        # tests if the username field has the attribute null=False
        expected_output = False
        is_null = Org._meta.get_field("username").null
        self.assertEqual(is_null, expected_output)


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

    def test_is_primary_key(self):
        # tests that the primary_key argument of the org field is set to true
        expected_result = True
        is_null = OrgLocation._meta.get_field("org").primary_key
        self.assertEqual(is_null, expected_result)

    def test_is_to_linked_to_org(self):
        # tests that the OneToOneField is linked to an org model
        expected_result = Org
        org = Org.objects.get(username="MyOrg")
        is_org = OrgLocation.objects.get(org=org).org.__class__
        self.assertEqual(is_org, expected_result)

    def test_is_on_delete_cascade(self):
        # tests that the on_delete argument of the org field is set to models.CASCADE
        expected_result = models.CASCADE
        is_cascade = OrgLocation._meta.get_field("org").remote_field.on_delete  # type: ignore
        self.assertEqual(is_cascade, expected_result)

    def test_is_org_blank(self):
        # tests that the blank argument of the org field is set to True
        expected_result = True
        is_blank = OrgLocation._meta.get_field("org").blank
        self.assertEqual(is_blank, expected_result)

    def test_is_country_unique(self):
        # tests that the unique argument of the country field is set to False
        expected_result = False
        is_unique = OrgLocation._meta.get_field("country").unique  # type: ignore
        self.assertEqual(is_unique, expected_result)

    def test_country_max_length(self):
        # tests the maximum length attribute of the country field
        expected_result = MAX_ORG_LOCATION_FIELD_LENGTH
        length = OrgLocation._meta.get_field("country").max_length
        self.assertEqual(length, expected_result)

    def test_is_region_unique(self):
        # tests if the unique argument of the region field is set to unique
        expected_result = False
        is_unique = OrgLocation._meta.get_field("region").unique  # type: ignore
        self.assertEqual(is_unique, expected_result)

    def test_region_max_length(self):
        # test that the max length argument of the region field is set to 50
        expected_result = MAX_ORG_LOCATION_FIELD_LENGTH
        length = OrgLocation._meta.get_field("region").max_length
        self.assertEqual(length, expected_result)

    def test_is_zip_unique(self):
        # tests if the unique argument of the zip field is set to unique
        expected_result = False
        is_unique = OrgLocation._meta.get_field("region").unique  # type: ignore
        self.assertEqual(is_unique, expected_result)

    def test_is_city_unique(self):
        # tests if the unique argument of the city field is set to unique
        expected_result = False
        is_unique = OrgLocation._meta.get_field("city").unique  # type: ignore
        self.assertEqual(is_unique, expected_result)

    def test_city_max_length(self):
        # tests the max_length argument of the city field
        expected_result = MAX_ORG_LOCATION_FIELD_LENGTH
        length = OrgLocation._meta.get_field("city").max_length
        self.assertEqual(length, expected_result)

    def test_is_street_address_unique(self):
        # tests if the unique argument of the street_address is unique
        expected_result = False
        is_unique = OrgLocation._meta.get_field("street_address").unique  # type: ignore
        self.assertEqual(is_unique, expected_result)

    def test_street_address_max_length(self):
        expected_result = MAX_ORG_LOCATION_FIELD_LENGTH
        length = OrgLocation._meta.get_field("street_address").max_length
        self.assertEqual(length, expected_result)
