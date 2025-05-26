from django.db import models

class Notice(models.Model):
    title = models.CharField("제목", max_length=200)
    content = models.TextField("내용")
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    is_pinned = models.BooleanField("상단 고정", default=False)

    class Meta:
        ordering = ['-is_pinned', '-created_at']

    def __str__(self):
        return self.title
