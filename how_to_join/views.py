# views.py
from django.shortcuts import render
from .models import ServerHowToJoin

def server_how_to_join(request):
    how_to_join = ServerHowToJoin.objects.all()
    return render(request, 'about_server/how_to_join.html', {'how_to_join': how_to_join})
