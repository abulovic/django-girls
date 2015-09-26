from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from .models import Post

## VIEWS ##
def homepage(request):
	return render(request, "homepage.html")

def latest_post(request):
	pass

def create(request):
	if request.method != "POST":
		raise Http404("Get outta here!")
	title = request.POST["title"]
	content = request.POST["content"]
	post = Post.objects.create(title=title, content=content)
	return redirect('/')

## URLS ##
urlpatterns = [
    url(r'^$', homepage),
    url(r'^latest-post$', latest_post),
    url(r'^create$', create)
]
