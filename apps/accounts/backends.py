
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class OrgBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            raise ValidationError("Invalid Username")
        else:
            if user.check_password(password):
                return user
            else:
                raise ValidationError("Invalid Password")

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return None