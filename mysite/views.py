from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from .models import Post


def homepage(request):
	return render(request, "homepage.html")

def create(request):
	if request.method != "POST":
		raise Http404("Get outta here!")
	title = request.POST["title"]
	content = request.POST["content"]
	post = Post.objects.create(title=title, content=content)
	return redirect('/')
