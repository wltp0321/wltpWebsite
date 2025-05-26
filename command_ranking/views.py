from django.shortcuts import render
from .models import Player
# Create your views here.


def command_ranking_main(request):
    players = Player.objects.all().order_by("rank")
    content = {"players": players}
    return render(request, "command_ranking/index.html", content)