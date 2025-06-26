from django.db import models

# Create your models here.

    
class BuildPlayer(models.Model):
    player = models.CharField(max_length=255, null=True, blank=True)
    point = models.IntegerField(null=True, blank=True)
    things = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.things
    

class RedstonePlayer(models.Model):
    player = models.CharField(max_length=255, null=True, blank=True)
    point = models.IntegerField(null=True, blank=True)
    things = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.things
    
class HardWorkedPlayer(models.Model):
    player = models.CharField(max_length=255, null=True, blank=True)
    playtime_txt = models.CharField(max_length=255, null=True, blank=True)
    playtime = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.player