from django.db import models


class User(models.Model):
    name = models.CharField(max_length=250, blank=False, verbose_name="User name")
    password = models.CharField(max_length=250, blank=False, verbose_name="Password")
    # TODO: tutorial redefine