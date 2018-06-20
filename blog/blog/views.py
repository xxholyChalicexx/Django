from django.http import HttpResponse
from django.shortcuts import render
def about(request):
	#return HttpResponse("This is the about file")
	return render(request, "about.html")

def index(request):
	#return HttpResponse("This is a homepage")
	return render(request, "home.html")