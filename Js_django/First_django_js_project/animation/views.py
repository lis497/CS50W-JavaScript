import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	# previously this is copied form posts application
	# however, when rendering "posts/animation/index.html"
	# eventhough this view and posts are inside the same folder
	# it goes back to call the previous folder in infinite template
	# change this folder name from posts to animations partially fixes
	return render(request, "animation/index.html")

def posts(request):
	start = int(request.GET.get("start") or 0)
	end = int(request.GET.get("end") or (start + 9))
	data = []
	for i in range(start, end + 1):
		data.append(f"Post #{i}")
	time.sleep(1)
	return JsonResponse({"posts": data})
