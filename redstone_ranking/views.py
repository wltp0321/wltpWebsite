from django.shortcuts import render
from .models import Player
# Create your views here.


def redstone_ranking_main(request):
    players = Player.objects.all().order_by("rank")
    content = {"players": players}
    return render(request, "redstone_ranking/index.html", content)