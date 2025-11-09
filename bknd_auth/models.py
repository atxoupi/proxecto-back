from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("An email is required")
        if not first_name:
            raise ValueError("A first name is required")
        if not last_name:
            raise ValueError("A last name is required")
        if not password:
            raise ValueError("A password is required")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.enabled = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(email, first_name, last_name, password)
        user.administrator = True
        user.save()
        return user


class User(AbstractBaseUser):
    class Meta:
        ordering = ["id"]

    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField()
    last_name = models.CharField()
    enabled = models.BooleanField(default=False)
    administrator = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return f"{self.email} ({self.id})"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return f"{self.first_name}"

    @property
    def is_superuser(self):
        return self.administrator

    def has_perm(self, perm, obj=None):
        return self.administrator


    @property
    def is_active(self):
        return self.enabled