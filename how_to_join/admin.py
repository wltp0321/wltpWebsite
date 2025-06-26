# admin.py
from django.contrib import admin
from .models import ServerHowToJoin

@admin.register(ServerHowToJoin)
class ServerHowToJoinAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'content0')
