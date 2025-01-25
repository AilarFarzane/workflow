from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    current_state = models.ForeignKey('statemanager.State', on_delete=models.CASCADE, null=True, blank=True)
