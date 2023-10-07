from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, name, password):
        if not name:
            raise ValueError(("The name must be set"))

        name = self.normalize_email(name)
        user = self.model(org_name=name)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, org_name, password):
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(org_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
