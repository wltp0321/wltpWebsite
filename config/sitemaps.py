from django.contrib.sitemaps import Sitemap
from .models import MyModel

class MyModelSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return MyModel.objects.all()

    def location(self, obj):
        return f"/my-model/{obj.pk}/"