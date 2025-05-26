from django.shortcuts import render

# Create your views here.

def about_server_main(request):
    return render(request, "about_server/index.html")

def rule_main(request):
	return render(request, "about_server/rule.html")

def join_main(request):
	return render(request, "about_server/how_to_join.html")

def description_main(request):
    return render(request, "about_server/description.html")

