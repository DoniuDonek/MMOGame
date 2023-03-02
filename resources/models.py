from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class Mineral(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_amount = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.user.username}'s Minerals"


class Gas(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Gas"


class Population(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    starting_amount = models.IntegerField(default=9)
    max_population = models.IntegerField(default=200)

    def __str__(self):
        return f"{self.user.username}'s Population"
    

User = get_user_model()

class GameProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    minerals = models.PositiveIntegerField(default=50)
    drones = models.PositiveIntegerField(default=5)