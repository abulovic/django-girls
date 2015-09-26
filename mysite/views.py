from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from .models import Post


def homepage(request):
	posts = Post.objects.all()
	return render(request, "homepage.html", {'posts': posts})

def create(request):
	if request.method != "POST":
		raise Http404("Get outta here!")
	title = request.POST["title"]
	content = request.POST["content"]
	post = Post.objects.create(title=title, content=content)
	return redirect('/')

def delete(request):
	Post.objects.all().delete()
	return redirect('/')
