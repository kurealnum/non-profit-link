from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class OrgBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if password and user.check_password(password):
                return user
        return None
