from django.core.exceptions import ValidationError
from project.validators import UniqueCharacterValidator
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password


class UniqueCharacterValidatorTestCases(TestCase):
    def setUp(self):
        self.instance = UniqueCharacterValidator()

    def test_validate_with_special_char_but_short_password(self):
        # tests that the password does not validate when the password is too short and there's a special character
        password = "abcde!"
        self.assertRaises(ValidationError, validate_password, password)

    def test_validate_with_special_char_but_long_password(self):
        # tests that the password is valid with a long password and a special character
        password = "abcdefghijklmono!"
        is_valid = validate_password(password)
        self.assertIsNone(is_valid)

    def test_validate_with_no_special_char_but_long_password(self):
        password = "goiaijnbiojamkwes"
        self.assertRaises(ValidationError, validate_password, password)

    def test_get_help_text(self):
        # just tests to make sure this returns what it should
        res = self.instance.get_help_text()
        self.assertEqual(type(res), str)
