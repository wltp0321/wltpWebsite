from django.contrib import admin
from .models import Building
# Register your models here.
@admin.register(Building)
class PlayerAdmin(admin.ModelAdmin):
    pass