from django.shortcuts import render
from .models import Player

def main_main(request):
	players = Player.objects.all()
	content = {"players": players}
	return render(request, "main/index.html", content)