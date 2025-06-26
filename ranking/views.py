from django.shortcuts import render
from .models import *

# Create your views here.
def ranking_main(request):
    TopBuildPlayer = BuildPlayer.objects.all().order_by('-point')[:3]
    TopRedstonePlayer = RedstonePlayer.objects.all().order_by('-point')[:3]

    context = {
        'BuildPlayers': TopBuildPlayer,
        'RedstonePlayers': TopRedstonePlayer
    }
    return render(request, 'ranking/index.html', context)

