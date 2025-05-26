from django.shortcuts import render

# Create your views here.
def gallery_main(request):
	return render(request, "gallery/index.html")
