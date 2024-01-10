from django.test import TestCase
from apps.accounts.models import Org


class OrgTestCases(TestCase):
    def setUp(self):
        Org.objects.create(username="MyOrg")

    def test_is_absolute_url(self):
        # makes sure the absolute url function returns the expected URL
        first_org = Org.objects.get(username="MyOrg")
        self.assertEqual(first_org.get_absolute_url(), "/nonprofits/homepage/1Org/")
