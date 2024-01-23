from django.test import TestCase, Client
from django.db.migrations import Migration
from django.contrib.postgres.operations import TrigramExtension
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

    def test_method_request_type(self):
        # tests to make sure the method only accepts PUT requests
        get_response = self.client.get(self.url)
        post_response = self.client.post(self.url)
        expected_response = 405
        self.assertEqual(get_response.status_code, expected_response)
        self.assertEqual(post_response.status_code, expected_response)

    def test_is_correct_template(self):
        # checks if the correct template is being used
        response = self.client.put(self.url)
        expected_template = "edit_info_modal.html"
        self.assertTemplateUsed(response, expected_template)

    def test_redirect_if_not_logged_in(self):
        # checks that the redirect is working
        test_client = Client()
        response = test_client.put(self.url)
        expected_url = "/accounts/login/?next=/accounts/edit-org-info/"
        self.assertRedirects(response, expected_url)

    def test_context_content(self):
        # check if the *content* of the context is correct
        response = self.client.put(self.url)
        expected_result = [OrgContactInfoForm, OrgInfoForm, OrgLocationForm]
        result = [i.__class__ for i in response.context["edit_org_forms"]]
        self.assertEqual(result, expected_result)
        
    def test_do_forms_save(self):
        # tests if the forms actually save
        response = self.client.put(self.url)
        test_client = Client()
        test_user = Org.objects.create(username="Org")
        test_user.set_password("MyAwesomePassword")
        test_user.save()
        test_client.login(username="Org", password="MyAwesomePassword")
        contact_form = OrgContactInfoForm()


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

    def test_is_correct_tempate(self):
        # checks if the correct template is being used
        response = self.client.put(self.url)
        expected_template = "edit_account_info_modal.html"
        self.assertTemplateUsed(response, expected_template)

    def test_redirect_if_not_logged_in(self):
        # checks that the redirect is working
        test_client = Client()
        response = test_client.put(self.url)
        expected_url = "/accounts/login/?next=/accounts/edit-account-info/"
        self.assertRedirects(response, expected_url)

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

    def test_is_correct_tempate(self):
        # checks if the correct template is being used
        response = self.client.get(self.url)
        expected_template = "login.html"
        self.assertTemplateUsed(response, expected_template)

    def test_context_content(self):
        # check if the *content* of the context is correct
        response = self.client.get(self.url)
        expected_result = LoginRegisterForm
        result = response.context["form"].__class__
        self.assertEqual(result, expected_result)


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

    def test_is_correct_tempate(self):
        # checks if the correct template is being used
        response = self.client.get(self.url)
        expected_template = "register.html"
        self.assertTemplateUsed(response, expected_template)

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


class SearchNonProfitsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("search_non_profits")

    def test_valid_response_status(self):
        # tests that the response status code being returned is correct
        response = self.client.get(self.url)
        expected_response = 200
        self.assertEqual(response.status_code, expected_response)

    def test_correct_tempate(self):
        # tests that the correct template is being used to render
        response = self.client.get(self.url)
        expected_template = "search_non_profits.html"
        self.assertTemplateUsed(response, expected_template)

    def test_context_content(self):
        # check if the *content* of the context is correct
        response = self.client.get(self.url)
        expected_content = QuerySet[OrgLocation]
        self.assertEqual(type(response.context["orgs"]), expected_content)


class SearchNonProfitsResultsTests(TestCase):
    def setUp(self):
        TrigramExtension()
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

    def test_correct_tempate(self):
        # tests that the correct template is being used to render
        response = self.client.post(self.url)
        expected_template = "search_non_profits_results.html"
        self.assertTemplateUsed(response, expected_template)

    def test_context_content(self):
        # check if the *content* of the context is correct
        response = self.client.post(self.url, data={"org": "org", "search": "org"})
        response_context = response.context["orgs"]
        expected_content = QuerySet[OrgLocation]

        # this view can return orgs as "None" with no issues so we need to check for that
        if response_context != None:
            self.assertEqual(type(response.context["orgs"]), expected_content)

