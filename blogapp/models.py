from django.db import models

# Create your models here.

class blog_database(models.Model):
	author = models.CharField(max_length=60)
	post = models.CharField(max_length=1000000)
	
