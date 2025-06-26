from django.db import models

class Notice(models.Model):
    title = models.CharField("title", max_length=200, null=True, blank=True)
    content0 = models.TextField("content0", null=True, blank=True)
    content1 = models.TextField("content1", null=True, blank=True)
    created_at = models.DateTimeField("createdAt", auto_now_add=True, null=True, blank=True)
    notice_type = models.IntegerField("noticeType", default=1, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
