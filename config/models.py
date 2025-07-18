# config/models.py
from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
