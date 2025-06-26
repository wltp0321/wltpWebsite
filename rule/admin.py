# admin.py
from django.contrib import admin
from .models import ServerRule

@admin.register(ServerRule)
class ServerRuleAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'content')
