from django.db import models
from django.contrib.auth import models as auth_user


class UserManager(auth_user.BaseUserManager):

    def create_user(self, username: str, password: str, is_staff=False, is_superuser=False) -> 'User':
        if not username:
            raise ValueError('The username must be set')
        user = self.model(username=username)
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser

        user.save()
        return user
    

    def create_superuser(self, username: str, password: str, is_staff=False, is_superuser=False) -> 'User':
        user = self.create_user(
            username = username,
            password = password,
            is_staff = True,
            is_superuser = True
        )

        user.save()
        return user


class User(auth_user.AbstractUser):
    username = models.CharField(max_length=255, blank=True, verbose_name="Username", unique=True)
    password = models.CharField(max_length=255, blank=True, verbose_name="Password")

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
