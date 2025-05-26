# views.py
from django.shortcuts import render
from .models import ServerRule

def server_rule(request):
    rules = ServerRule.objects.all()
    return render(request, 'about_server/rule.html', {'rules': rules})
