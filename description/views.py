# views.py
from django.shortcuts import render
from .models import ServerDescription

def server_descriptions(request):
    descriptions = ServerDescription.objects.all()
    return render(request, 'about_server/description.html', {'descriptions': descriptions})
