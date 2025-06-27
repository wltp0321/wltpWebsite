from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Player name")

    def __str__(self):
        return self.name
