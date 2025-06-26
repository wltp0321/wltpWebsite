# models.py
from django.db import models

class ServerRule(models.Model):
    order = models.PositiveIntegerField("order", default=0)
    title = models.TextField("title", null=True, blank=True)
    content = models.TextField("content", null=True, blank=True)

    class Meta:
        ordering = ['order']  # 순서대로 정렬

    def __str__(self):
        return f"{self.title}. {self.content[:20]}"
