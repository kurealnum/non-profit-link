from django.test import TestCase, Client
from apps.accounts.models import Org, OrgLocation, OrgInfo, OrgContactInfo
from django.urls import reverse


class HomepageTests(TestCase):
    def setUp(self):
        self.client = Client()
        instance = Org.objects.create(username="MyOrg")
        OrgLocation.objects.create(
            org=instance,
            country="US",
            region="Virginia",
            zip=12345,
            city="TomorrowLand",
            street_address="Awesome Address!",
        )
        OrgInfo.objects.create(org=instance)
        OrgContactInfo.objects.create(
            org=instance, phone=12345, email="awesome@gmail.com"
        )

    def test_correct_url(self):
        # just checks if the view works when the url is correct
        url = reverse("homepage", args=("MyOrg",))
        response = self.client.get(url)
        expected_status = 200
        status = response.status_code
        self.assertEqual(status, expected_status)

    def test_wrong_url(self):
        # checks that the view redirects when the url is wrong
        url = reverse("homepage", args=("IDon'tExist",))
        response = self.client.get(url)
        expected_redirect = reverse("org_does_not_exist")
        self.assertRedirects(response, expected_redirect)
