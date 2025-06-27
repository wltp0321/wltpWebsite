from django.shortcuts import render
from .models import *

# Create your views here.
def ranking_main(request):
    TopBuildPlayers = BuildPlayer.objects.all().order_by('-point')[:3]
    TopRedstonePlayers = RedstonePlayer.objects.all().order_by('-point')[:3]

    context = {
        'BuildPlayers': TopBuildPlayers,
        'RedstonePlayers': TopRedstonePlayers
    }
    return render(request, 'ranking/index.html', context)


def build_ranking_main(request):
    BuildPlayers = BuildPlayer.objects.all().order_by('-point')

    context = {
        'BuildPlayers': BuildPlayers,
    }
    return render(request, 'ranking/build_ranking.html', context)

def hard_worked_player_ranking_main(request):
    HardWorkedPlayers = HardWorkedPlayer.objects.all().order_by('-playtime')
    
    context = {
        'HardWorkedPlayers': HardWorkedPlayers,
    }
    return render(request, 'ranking/hard_worked_ranking.html', context)

def redstone_player_ranking_main(request):
    RedstonePlayers = RedstonePlayer.objects.all().order_by('-point')
    
    context = {
        'RedstonePlayers': RedstonePlayers,
    }
    return render(request, 'ranking/redstone_ranking.html', context)