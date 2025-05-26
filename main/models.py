from django.db import models

# Create your models here.
class Player(models.Model):
    nickname = models.CharField(max_length=255, blank=True, null=True)
    skinurl = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.nickname