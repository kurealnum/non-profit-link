from django.test import TestCase
from apps.accounts.models import Org
from django.db.utils import IntegrityError

MAX_USERNAME_LENGTH = 100


class OrgTestCases(TestCase):
    def setUp(self):
        Org.objects.create(username="MyOrg")

    def test_is_absolute_url(self):
        # makes sure the absolute url function returns the expected URL
        first_org = Org.objects.get(username="MyOrg")
        expected_output = "/nonprofits/homepage/MyOrg/"
        self.assertEqual(first_org.get_absolute_url(), expected_output)

    def test_str_method(self):
        # tests if the __str__ function in Org returns the expected value
        first_org = Org.objects.get(username="MyOrg")
        expected_output = str(first_org)
        self.assertEqual(first_org.username, expected_output)

    def test_uniqueness(self):
        # tests if the model's username attribute is set to unique
        with self.assertRaises(IntegrityError):
            Org.objects.create(username="MyOrg")

    def test_max_length(self):
        # tests the maximum length of username
        expected_output = MAX_USERNAME_LENGTH
        max_length = Org._meta.get_field("username").max_length
        self.assertEqual(max_length, expected_output)

    def test_is_null(self):
        # tests if the username field is set to null=False
        expected_output = False
        is_null = Org._meta.get_field("username").null
        self.assertEqual(is_null, expected_output)
