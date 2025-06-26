from django.contrib import admin
from .models import *

@admin.register(BuildPlayer)
class BuildPlayerAdmin(admin.ModelAdmin):
    list_display = ('player', 'point', 'things')
    search_fields = ('player', 'things')

@admin.register(RedstonePlayer)
class RedstonePlayerAdmin(admin.ModelAdmin):
    list_display = ('player', 'point', 'things')
    search_fields = ('player', 'things')

@admin.register(HardWorkedPlayer)
class HardWorkedPlayerAdmin(admin.ModelAdmin):
    list_display = ('player', 'playtime')
    search_fields = ('player',)
