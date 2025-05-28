from django.http import HttpResponse

def Ads(request):

    return HttpResponse("google.com, pub-2878829375668478, DIRECT, f08c47fec0942fa0", content_type='text/plain')