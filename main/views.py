from django.shortcuts import render
from .models import Player

def main_main(request):
	players = Player.objects.all()
	content = {"players": players}
	return render(request, "main/index.html", content)



from django.http import HttpResponse

def Ads(request):

    return HttpResponse("google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0", content_type='text/plain')
