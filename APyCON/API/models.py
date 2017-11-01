from django.db import models
from django.contrib.auth.models import User

class Speaker(models.Model):
	usuario= models.Foreignkey(User)
	twitter =  models.CharField(max_length = 200)
	biografia = models.TextField(max_length=1000)
	dni = models.IntegerField()
	talk = models.CharField(max_length = 200)

