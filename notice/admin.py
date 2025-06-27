from django.contrib import admin
from .models import *

@admin.register(ImportantNotice)
class ImportantNoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content0', 'content1')
    ordering = ('-created_at',)

@admin.register(NormalNotice)
class NormalNoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content0', 'content1')
    ordering = ('-created_at',)

@admin.register(ArchivedNotice)
class ArchiveNoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content0', 'content1')
    ordering = ('-created_at',)
