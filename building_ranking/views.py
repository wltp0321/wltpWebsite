from django.shortcuts import render
from .models import Building
# Create your views here.


def building_ranking_main(request):
    buildings = Building.objects.all().order_by("rank")
    content = {"buildings": buildings}
    return render(request, "building_ranking/index.html", content)