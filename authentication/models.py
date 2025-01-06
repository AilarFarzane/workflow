from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    state = models.ForeignKey('statemanager.state', on_delete=models.CASCADE, null=True, blank=True)
