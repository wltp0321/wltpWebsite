from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse

def notice_list(request):
    ImportantNotices = ImportantNotice.objects.all()
    NormalNotices = NormalNotice.objects.all()
    ArchivedNotices = ArchivedNotice.objects.all()
    return render(request, 'notice/index.html', {'ImportantNotices': ImportantNotices, 'NormalNotices': NormalNotices, 'ArchivedNotices': ArchivedNotices})

def archived_notice(request, notice_id):
    notice = get_object_or_404(ArchivedNotice, id=notice_id)
    return render(request, 'notice/archived_notice.html', {'notice': notice})