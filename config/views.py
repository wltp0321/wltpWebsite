from django.http import HttpResponse

def Ads(request):

    return HttpResponse("google.com, pub-2878829375668478, DIRECT, f08c47fec0942fa0", content_type='text/plain')

def robots(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /private/",
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
