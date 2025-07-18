from django.db import models
from django.utils import timezone
from django.contrib.sites.models import Site

class ImportantNotice(models.Model):
    title = models.CharField("title", max_length=200, null=True, blank=True)
    content0 = models.TextField("content0", null=True, blank=True)
    content1 = models.TextField("content1", null=True, blank=True)
    created_at = models.DateTimeField("createdAt", default=timezone.now, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    

class NormalNotice(models.Model):
    title = models.CharField("title", max_length=200, null=True, blank=True)
    content0 = models.TextField("content0", null=True, blank=True)
    content1 = models.TextField("content1", null=True, blank=True)
    created_at = models.DateTimeField("createdAt", default=timezone.now, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class ArchivedNotice(models.Model):
    title = models.CharField("title", max_length=200, null=True, blank=True)
    content0 = models.TextField("content0", null=True, blank=True)
    content1 = models.TextField("content1", null=True, blank=True)
    created_at = models.DateTimeField("createdAt", default=timezone.now, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
