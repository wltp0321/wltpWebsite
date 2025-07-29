# admin.py
from django.contrib import admin
from .models import MarkdownDocument

@admin.register(MarkdownDocument)
class MarkdownDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')  # id 필드 추가
    fields = ("title", "content", "created_at")