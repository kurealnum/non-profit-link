from django.test import TestCase, Client
from django.db.models.query import QuerySet
from django.urls import reverse
from apps.accounts.models import Org, OrgContactInfo, OrgInfo, OrgLocation
from apps.accounts.forms import (
    LoginRegisterForm,
    OrgForm,
    OrgContactInfoForm,
    OrgInfoForm,
    OrgLocationForm,
)


class EditOrgInfoTests(TestCase):
    def setUp(self):
        # this client will be logged in. if you want a logged out client, remake it with Client()
        self.client = Client()
        self.url = reverse("edit_org_info")
        user = Org.objects.create(username="MyOrg")
        OrgContactInfo.objects.create(org=user, phone=123, email="MyEmail@gmail.com")
        OrgInfo.objects.create(org=user, desc="Awesome!", website="google.com")
        OrgLocation.objects.create(
            org=user,
            country="USA",
            region="California",
            zip=12345,
            city="MyAwesomeCity",
            street_address="12345 Awesome Ln",
        )
        user.set_password("THISismyAMAZINGPa$$sword")
        user.save()
        self.client.login(username="MyOrg", password="THISismyAMAZINGPa$$sword")

        # self.factory = RequestFactory()

    def test_method_request_type(self):
        # tests to make sure the method only accepts PUT requests
        get_response = self.client.get(self.url)
        expected_response = 405
        self.assertEqual(get_response.status_code, expected_response)

    def test_redirect_if_not_logged_in(self):  # checks that the redirect is working
        test_client = Client()
        response = test_client.put(self.url)
        expected_url = "/accounts/login/?next=/accounts/edit-org-info/"
        self.assertRedirects(response, expected_url)

    # def test_is_200_if_valid(self):
    #     # tests that the view returns a 200 if the forms are valid
    #     edit_info_data = {
    #         "country": "USA",
    #         "region": "Florida",
    #         "zip": 12345,
    #         "city": "Florida man",
    #         "street_address": "12345 Awesome Lane",
    #         "phone": 123456,
    #         "email": "myemail@gmail.com",
    #         "desc": "We are awesome!",
    #         "website": "google.com",
    #     }
    #     request = self.factory.put(self.url)
    #     request.body = edit_info_data
    #     response = edit_org_info(request)

    # expected_status = 201
    # status = response.status_code
    # self.assertEqual(status, expected_status)

    def test_context_content(self):
        # check if the *content* of the context is correct
        response = self.client.put(self.url)
        expected_result = [OrgContactInfoForm, OrgInfoForm, OrgLocationForm]
        result = [i.__class__ for i in response.context["edit_org_forms"]]
        self.assertEqual(result, expected_result)


class EditAccountInfoTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("edit_account_info")
        user = Org.objects.create(username="MyOrg")
        user.set_password("THISismyAMAZINGPa$$sword")
        user.save()
        self.client.login(username="MyOrg", password="THISismyAMAZINGPa$$sword")

    def test_method_request_type(self):
        # tests to make sure the method only accepts PUT requests
        get_response = self.client.get(self.url)
        post_response = self.client.post(self.url)
        expected_response = 405
        self.assertEqual(get_response.status_code, expected_response)
        self.assertEqual(post_response.status_code, expected_response)

    def test_redirect_if_not_logged_in(self):
        # checks that the redirect is working
        test_client = Client()
        response = test_client.put(self.url)
        expected_url = "/accounts/login/?next=/accounts/edit-account-info/"
        self.assertRedirects(response, expected_url)

    def test_status_and_context_valid_when_form_valid(self):
        # TODO
        pass

    def test_context_content(self):
        # check if the *content* of the context is correct
        response = self.client.put(self.url)
        expected_result = OrgForm
        result = response.context["edit_info_form"].__class__
        self.assertEqual(result, expected_result)


class LoginUserTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("login")
        user = Org.objects.create(username="MyOrg")
        user.set_password("THISismyAMAZINGPa$$sword")
        user.save()
        self.client.login(username="MyOrg", password="THISismyAMAZINGPa$$sword")

    def test_method_request_type(self):
        # tests to make sure the method returns the appropriate value for the request type
        get_response = self.client.get(self.url)
        post_response_no_credentials = self.client.post(self.url)
        expected_get_response = 200
        expected_post_response_no_credentials = 200
        self.assertEqual(get_response.status_code, expected_get_response)
        self.assertEqual(
            post_response_no_credentials.status_code,
            expected_post_response_no_credentials,
        )

    def test_redirects_on_correct_credentials(self):
        # tests if the view redirects the user when they have the correct credentials
        credentials = {"username": "MyOrg", "password": "THISismyAMAZINGPa$$sword"}
        post_response = self.client.post(self.url, data=credentials)
        expected_url = "/nonprofits/dashboard/"
        self.assertRedirects(post_response, expected_url)

    def test_issue_with_username(self):
        credentials = {"username": "wrongname", "password": "THISismyAMAZINGPa$$sword"}
        post_response = self.client.post(self.url, data=credentials)
        self.assertTrue(post_response.context["form"].errors != None)

    def test_issue_with_password(self):
        credentials = {"username": "MyOrg", "password": "wrongpassword"}
        post_response = self.client.post(self.url, data=credentials)
        self.assertTrue(post_response.context["form"].errors != None)

    def test_context_content(self):
        # check if the *content* of the context is correct
        response = self.client.get(self.url)
        expected_result = LoginRegisterForm
        result = response.context["form"].__class__
        self.assertEqual(result, expected_result)
        self.assertTrue(response.context["form"].errors != None)


class RegisterUserTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("register")
        user = Org.objects.create(username="MyOrg")
        user.set_password("THISismyAMAZINGPa$$sword")
        user.save()
        self.client.login(username="MyOrg", password="THISismyAMAZINGPa$$sword")

    def test_valid_response_status(self):
        post_response = self.client.get(self.url)
        get_response = self.client.get(self.url)
        expected_post_response = 200
        expected_get_response = 200
        self.assertEqual(expected_post_response, post_response.status_code)
        self.assertEqual(expected_get_response, get_response.status_code)

    def test_context_content(self):
        # check if the *content* of the context is correct
        response = self.client.get(self.url)
        expected_result = [OrgForm, OrgLocationForm, OrgContactInfoForm, OrgInfoForm]
        result = [i.__class__ for i in response.context["forms"]]
        self.assertEqual(result, expected_result)

    def test_redirect(self):
        # tests that the redirect works when the register information is correct
        test_client = Client()
        register_data = {
            "username": "TestOrg",
            "password": "myAWESOME1133!@",
            "confirm_password": "myAWESOME1133!@",
            "country": "USA",
            "region": "Florida",
            "zip": 12345,
            "city": "Florida man",
            "street_address": "12345 Awesome Lane",
            "phone": 123456,
            "email": "myemail@gmail.com",
            "desc": "We are awesome!",
            "website": "google.com",
        }
        response = test_client.post(self.url, data=register_data)
        expected_redirect = reverse("login")
        self.assertRedirects(response, expected_redirect)

    def tests_result_if_pass_invalid(self):
        # tests the output if the password is invalid
        register_data = {
            "username": "TestOrg",
            "password": "myAWESOME1133!@",
            "confirm_password": "wrongpassword",
            "country": "USA",
            "region": "Florida",
            "zip": 12345,
            "city": "Florida man",
            "street_address": "12345 Awesome Lane",
            "phone": 123456,
            "email": "myemail@gmail.com",
            "desc": "We are awesome!",
            "website": "google.com",
        }
        test_client = Client()
        response = test_client.post(self.url, data=register_data)
        # this should be 200, because the template still renders. errors are just added to the form
        expected_status = 200
        status = response.status_code
        self.assertEqual(status, expected_status)


class SearchNonProfitsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("search_non_profits")

    def test_valid_response_status(self):
        # tests that the response status code being returned is correct
        response = self.client.get(self.url)
        expected_response = 200
        self.assertEqual(response.status_code, expected_response)

    def test_context_content(self):
        # check if the *content* of the context is correct
        response = self.client.get(self.url)
        expected_content = QuerySet[OrgLocation]
        self.assertEqual(type(response.context["orgs"]), expected_content)


class SearchNonProfitsResultsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("search_non_profits_results")
        test_org = Org.objects.create(username="MyOrg")
        OrgLocation.objects.create(
            org=test_org,
            country="USA",
            region="California",
            zip=12345,
            city="MyAwesomeCity",
            street_address="12345 Awesome Ln",
        )

    def test_valid_response_status(self):
        # tests that the response status code being returned is correct
        response = self.client.post(self.url)
        expected_response = 200
        self.assertEqual(response.status_code, expected_response)

    def test_context_content_with_org(self):
        # check if the *content* of the context is correct when org = location
        response = self.client.post(self.url, data={"org": "org", "search": "org"})
        response_context = response.context["orgs"]
        expected_content = QuerySet[OrgLocation]

        self.assertTrue(
            response_context == None or type(response_context) == expected_content
        )

    def test_context_content_with_location_country(self):
        # check if the content of the context is correct when org = location
        response = self.client.post(
            self.url,
            data={"org": "location", "search": "USA", "location-options": "country"},
        )
        response_context = response.context["orgs"]
        expected_content = QuerySet[OrgLocation]

        self.assertTrue(type(response_context) == expected_content)

    def test_context_content_with_location_region(self):
        # check if the content of the context is correct when org = location
        response = self.client.post(
            self.url,
            data={
                "org": "location",
                "search": "California",
                "location-options": "region",
            },
        )
        response_context = response.context["orgs"]
        expected_content = QuerySet[OrgLocation]

        self.assertTrue(type(response_context) == expected_content)

    def test_context_content_with_location_zipcode(self):
        # check if the content of the context is correct when org = location
        response = self.client.post(
            self.url,
            data={"org": "location", "search": "12345", "location-options": "zipcode"},
        )
        response_context = response.context["orgs"]
        expected_content = QuerySet[OrgLocation]

        self.assertTrue(type(response_context) == expected_content)

    def test_context_content_with_location_city(self):
        # check if the content of the context is correct when org = location
        response = self.client.post(
            self.url,
            data={
                "org": "location",
                "search": "MyAwesomeCity",
                "location-options": "city",
            },
        )
        response_context = response.context["orgs"]
        expected_content = QuerySet[OrgLocation]

        self.assertTrue(type(response_context) == expected_content)

    def test_context_content_with_location_street_address(self):
        # check if the content of the context is correct when org = location
        response = self.client.post(
            self.url,
            data={
                "org": "location",
                "search": "12345 Awesome Ln",
                "location-options": "street-address",
            },
        )
        response_context = response.context["orgs"]
        expected_content = QuerySet[OrgLocation]

        self.assertTrue(type(response_context) == expected_content)
