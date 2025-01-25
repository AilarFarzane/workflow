from pkgutil import get_data

from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model


User = get_user_model()


class State(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    COLOR_CHOICES =[
        ("#0000FF", "blue", ),
        ("#00FF00", "green", ),
        ("#FF0000", "red", ),
    ]
    color = ColorField(choices=COLOR_CHOICES)

    def __str__(self):
        return self.name



class Action(models.Model):
    starting_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='starting_state')
    ending_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='ending_state')
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug  = models.SlugField(max_length=100, unique=True)
    COLOR_CHOICES = [
        ("#00FF00", "green",),
        ("#FF0000", "red",),
        ("#0000FF", "blue",)
    ]
    color = ColorField(choices=COLOR_CHOICES)

    def __str__(self):
        return self.name




class ActionStatePath(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, blank=True, null=True, related_name='action')

    @property
    def current_state(self):
        return self.user.state.name

    def save(self, *args, **kwargs):
       if self.user and hasattr(self.user, 'state'):
           self._current_state = self.user.state.name
       super().save(*args, **kwargs)

    def __str__(self):
        return f"user: {self.user.username}"



