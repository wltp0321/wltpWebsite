# models.py
from django.db import models

class ServerHowToJoin(models.Model):
    order = models.PositiveIntegerField("order", default=0)
    title = models.TextField("title", null=True, blank=True)
    content0 = models.TextField("content0", null=True, blank=True)
    content1 = models.TextField("content1", null=True, blank=True)

    class Meta:
        ordering = ['order']  # 순서대로 정렬

    def __str__(self):
        title = self.title or ""
        content0 = self.content0 or ""
        content1 = self.content1 or ""
        return f"{title}. {content0[:20]}. {content1[:20]}"

