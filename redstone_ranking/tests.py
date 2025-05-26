from django.test import TestCase

# Create your tests here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass