import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "posts/index.html")


def test_api_with_apihtml(request):
	# this is the tests with api.html which has html content
	# Get start and end points
	start = int(request.GET.get("start") or 0)
	end = int(request.GET.get("end") or (start + 9))

	# Generate list of posts
	data = []
	for i in range(start, end + 1):
		data.append(f"Post #{i}")
	
	# Artificially delay speed of response
	time.sleep(1)

	return render(request,"posts/api.html",{
			"data": data
		})
	

def posts(request):
	start = int(request.GET.get("start") or 0)
	end = int(request.GET.get("end") or (start + 9))
	data = []
	for i in range(start, end + 1):
		data.append(f"Post #{i}")
	time.sleep(1)
	return JsonResponse({"posts": data})
