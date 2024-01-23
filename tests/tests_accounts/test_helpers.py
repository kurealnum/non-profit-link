from django.test import TestCase
from apps.accounts.helpers import add_errors_to_password


class AddErrorsToPasswordTests(TestCase):
    def test_password_throws_correct_error(self):
        # tests that the correct string is returned when the password doesn't meet the requirements
        bad_password = "abcde"
        expected_value = "Your password does not meet the requirements!" 
        result = add_errors_to_password(bad_password, bad_password)
        self.assertEqual(result, expected_value)

    def test_password_matches_password(self):
        # tests that the correct string is returned when the 2 passwords don't equal eachother
        password_1 = "MyVery1234Secure!!Password"
        password_2 = "MyVery234NotTheSame!!Password"
        result = add_errors_to_password(password_1, password_2)
        expected_result = "Your passwords do not match!"
        self.assertEqual(result, expected_result)


