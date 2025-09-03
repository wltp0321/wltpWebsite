from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import MarkdownDocument
import markdown
import re

def Ads(request):
    return HttpResponse("google.com, pub-2878829375668478, DIRECT, f08c47fec0942fa0", content_type='text/plain')

def robots(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "User-agent: Yeti",
        "Allow: /",
        "Sitemap: https://www.wltp.world/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def sitemap(request):
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        '  <url><loc>https://www.wltp.world/rules/</loc></url>',
        '  <url><loc>https://www.wltp.world/how_to_join/</loc></url>',
        '  <url><loc>https://www.wltp.world/descriptions/</loc></url>',
        '  <url><loc>https://www.wltp.world/</loc></url>',
        '  <url><loc>https://www.wltp.world/ranking/</loc></url>',
        '  <url><loc>https://www.wltp.world/ranking/build_ranking/</loc></url>',
        '  <url><loc>https://www.wltp.world/ranking/redstone_ranking/</loc></url>',
        '  <url><loc>https://www.wltp.world/ranking/hard_worked_ranking/</loc></url>',
        '  <url><loc>https://www.wltp.world/notices/</loc></url>',
        '  <url><loc>https://www.wltp.world/account/login/</loc></url>',
        '  <url><loc>https://www.wltp.world/account/signup/</loc></url>',
        '</urlset>'
    ]
    return HttpResponse("\n".join(lines), content_type="application/xml")

import re

def replace_checkboxes(html):
    # 체크된 박스 (disabled + checked) → ✅
    html = re.sub(
        r'<input[^>]*type=["\']checkbox["\'][^>]*disabled[^>]*checked[^>]*\/?>',
        '✅',
        html,
        flags=re.IGNORECASE
    )
    # 체크 안 된 박스 (disabled, checked 없는) → ⬛
    html = re.sub(
        r'<input[^>]*type=["\']checkbox["\'][^>]*disabled(?![^>]*checked)[^>]*\/?>',
        '⬛',
        html,
        flags=re.IGNORECASE
    )
    return html


def docs_detail_view(request, doc_id):
    doc = get_object_or_404(MarkdownDocument, id=doc_id)
    raw_html = markdown.markdown(
        doc.content,
        extensions=[
            'fenced_code',
            'codehilite',
            'tables',
            'pymdownx.tilde',
            'pymdownx.tasklist',
        ],
        extension_configs={
            'pymdownx.tasklist': {'custom_checkbox': False}
        }
    )
    
    content = replace_checkboxes(raw_html)
    return render(request, 'docs/docs_detail.html', {
        'doc': doc,
        'content': content,
    })

def docs_list(request):
    docs = MarkdownDocument.objects.order_by('-created_at')
    return render(request, 'docs/docs_list.html', {'docs': docs})
