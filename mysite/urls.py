from django.conf.urls import include, url
from django.contrib import admin
from django.template.context_processors import csrf

from .views import *

## URLS ##
urlpatterns = [
    url(r'^$', homepage),
    url(r'^create$', create),
    url(r'^delete$', delete),
]
