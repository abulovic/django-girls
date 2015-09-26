from django.db import models
from django.utils import timezone


## MODELS ##
class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date_created = models.DateTimeField(default=timezone.now)