from os import name
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.username
