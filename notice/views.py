from django.shortcuts import render
from .models import Notice

def notice_list(request):
    notices = Notice.objects.all()
    return render(request, 'notice/index.html', {'notices': notices})
