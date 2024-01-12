from django.test import TestCase, Client
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

    def test_is_correct_tempate(self):
        # checks if the correct template is being used
        response = self.client.put(self.url)
        expected_template = "edit_info_modal.html"
        self.assertTemplateUsed(response, expected_template)

    def test_correct_context(self):
        # checks if the context is correct
        response = self.client.put(self.url)
        expected_response = "edit_org_forms"
        self.assertIn(expected_response, response.context)

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

    def test_correct_context(self):
        # checks if the context is correct
        response = self.client.put(self.url)
        expected_response = "edit_info_form"
        self.assertIn(expected_response, response.context)

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
        # TODO possibly differnet response for redirect?
        get_response = self.client.get(self.url)
        post_response = self.client.post(self.url)
        expected_get_response = 201
        expected_post_response = 201
        self.assertEqual(get_response.status_code, expected_get_response)
        self.assertEqual(post_response.status_code, expected_post_response)

    def test_is_correct_tempate(self):
        # checks if the correct template is being used
        # TODO add checks for redirect
        response = self.client.get(self.url)
        expected_template = "login.html"
        self.assertTemplateUsed(response, expected_template)

    def test_correct_context(self):
        # checks if the context is correct
        response = self.client.get(self.url)
        expected_response = "form"
        self.assertIn(expected_response, response.context)

    def test_redirect_if_not_logged_in(self):
        # checks that the redirect is working
        # TODO this view is not a login required view, so
        # we just need to check that it redirects on successful login
        test_client = Client()
        response = test_client.get(self.url)
        expected_url = "/accounts/login/?next=/accounts/edit-account-info/"
        self.assertRedirects(response, expected_url)

    def test_context_content(self):
        # check if the *content* of the context is correct
        response = self.client.get(self.url)
        expected_result = LoginRegisterForm
        result = response.context["form"].__class__
        self.assertEqual(result, expected_result)
