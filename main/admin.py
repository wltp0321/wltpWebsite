from django.contrib import admin

# Register your models here.
from .models import Player
# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass