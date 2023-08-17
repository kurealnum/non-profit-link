from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    objects = CustomUserManager()

    non_profit_name = models.CharField(unique=False, max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = () # type: ignore

    def __str__(self) -> str:
        return self.email