from django.test import TestCase
from apps.accounts.backends import OrgBackend
from apps.accounts.models import Org


class AuthenticateTestCases(TestCase):
    def setUp(self):
        self.user = Org.objects.create(username="MyOrg")
        self.user.set_password("MyAwesomeSECURE!!Pass")
        self.user.save()

    def test_method_returns_none(self):
        # tests that the method returns none for both cases that it should return none
        expected_result = None
        instance = OrgBackend()
        first_result = instance.authenticate(
            username="NotReal", password="awesomePassword"
        )
        second_result = instance.authenticate(
            username="MyOrg", password="TheWrongPassword"
        )
        self.assertEqual(expected_result, first_result)
        self.assertEqual(expected_result, second_result)

    def test_method_returns_user_object(self):
        # tests that the method returns a user object with correct credentials
        instance = OrgBackend()
        result = instance.authenticate(
            username="MyOrg", password="MyAwesomeSECURE!!Pass"
        )
        self.assertEqual(type(result), Org)
