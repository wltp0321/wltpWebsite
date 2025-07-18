# core/views.py
from django.http import JsonResponse
from notice.models import *

def important_notices(request):
    notices = ImportantNotice.objects.order_by('-created_at')
    results = []
    for notice in notices:
        results.append({
            'id': notice.id,
            'title': notice.title,
            'content0': notice.content0,
            'content1': notice.content1,
            'created_at': notice.created_at.strftime('%Y-%m-%d %H:%M')
        })
    return JsonResponse(results, safe=False)

def normal_notices(request):
    notices = NormalNotice.objects.order_by('-created_at')
    results = []
    for notice in notices:
        results.append({
            'id': notice.id,
            'title': notice.title,
            'content0': notice.content0,
            'content1': notice.content1,
            'created_at': notice.created_at.strftime('%Y-%m-%d %H:%M')
        })
    return JsonResponse(results, safe=False)

def archived_notices(request):
    notices = ArchivedNotice.objects.order_by('-created_at')
    results = []
    for notice in notices:
        results.append({
            'id': notice.id,
            'title': notice.title,
            'content0': notice.content0,
            'content1': notice.content1,
            'created_at': notice.created_at.strftime('%Y-%m-%d %H:%M')
        })
    return JsonResponse(results, safe=False)