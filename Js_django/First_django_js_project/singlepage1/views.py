from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "singlepage1/index.html")

texts = ["Orange cat", "Pink", "Meow meow hug"]

def section(request, num):
	if 1 <= num <= 3:
		return HttpResponse(texts[num - 1])
	else:
		raise Http404("No such section")