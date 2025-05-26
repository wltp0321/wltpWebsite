from django.shortcuts import render
from .models import Player
# Create your views here.


def build_ranking_main(request):
    players = Player.objects.all().order_by("rank")
    content = {"players": players}
    return render(request, "build_ranking/index.html", content)