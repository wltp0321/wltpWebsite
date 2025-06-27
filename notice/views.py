from django.shortcuts import render
from .models import *

def notice_list(request):
    ImportantNotices = ImportantNotice.objects.all()
    NormalNotices = NormalNotice.objects.all()
    ArchivedNotices = ArchivedNotice.objects.all()
    return render(request, 'notice/index.html', {'ImportantNotices': ImportantNotices, 'NormalNotices': NormalNotices, 'ArchivedNotices': ArchivedNotices})
