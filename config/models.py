    # config/models.py
from django.db import models
from django.utils import timezone
class MyModel(models.Model):
    title = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class MarkdownDocument(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  # 마크다운 텍스트
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
