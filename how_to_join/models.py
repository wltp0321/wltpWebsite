# models.py
from django.db import models

class ServerHowToJoin(models.Model):
    order = models.PositiveIntegerField("표시 순서", default=0)
    content = models.TextField("내용")

    class Meta:
        ordering = ['order']  # 순서대로 정렬

    def __str__(self):
        return f"{self.order}. {self.content[:20]}"
