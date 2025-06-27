from django.shortcuts import render
from .models import *
from ranking.models import *

def main_main(request):
    count = Player.objects.count()
    build =  BuildPlayer.objects.count()
    redstone =  RedstonePlayer.objects.count()
    return render(request, "main/index.html", {'player_count': count, 'build_player_count': build, 'redstone_player_count': redstone})





from django.http import HttpResponse

def Ads(request):

    return HttpResponse("google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0", content_type='text/plain')
