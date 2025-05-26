from django.db import models

# Create your models here.
class Player(models.Model):
    nickname = models.CharField(max_length=255)
    point = models.CharField(max_length=255)
    rank = models.IntegerField(default=0)
    tier = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.nickname