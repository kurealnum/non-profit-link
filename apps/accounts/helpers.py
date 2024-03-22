from django.contrib.auth.password_validation import validate_password
from django.forms import ValidationError


def add_errors_to_password(password, confirm_password):
    # check if password is even valid
    try:
        validate_password(password)
    except ValidationError as e:
        return e

    # check if password = confirm password
    if password != confirm_password:
        return "Your passwords do not match!"

    return None
