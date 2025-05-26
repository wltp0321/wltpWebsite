from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_pinned', 'created_at')
    list_filter = ('is_pinned', 'created_at')
    search_fields = ('title', 'content')
