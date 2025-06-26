# admin.py
from django.contrib import admin
from .models import ServerDescription

@admin.register(ServerDescription)
class ServerDescriptionAdmin(admin.ModelAdmin):
    list_display = ('order', 'emoji', 'title', 'content')
