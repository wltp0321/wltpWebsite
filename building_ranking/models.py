from django.db import models

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=255)
    point = models.CharField(max_length=255)
    rank = models.IntegerField(default=0)
    img = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name