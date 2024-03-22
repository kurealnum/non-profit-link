from django.core.exceptions import ValidationError
from django.utils.translation import gettext


# ensures there's a unique character in the password (non-unique chars include nums)
class UniqueCharacterValidator:
    def __init__(self):
        pass

    def validate(self, password, user=None):
        password_has_unique_chars = False
        for c in password:
            if (
                not (47 < ord(c) < 58)
                and not (64 < ord(c) < 91)
                and not (96 < ord(c) < 123)
            ):
                password_has_unique_chars = True

        if not password_has_unique_chars:
            raise ValidationError(
                gettext(
                    "This password must contain at least one special character that is not a number!"
                ),
                code="no_unique_chars",
            )

    def get_help_text(self):
        return gettext("Your password must contain at least one special character!")
