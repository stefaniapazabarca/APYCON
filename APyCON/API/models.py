from django.db import models

class Speaker(models.Model):
	twitter =  models.CharField(max_length= 200)
	biography = models.TextField(max_length= 1000)
	idnum = models.IntegerField()
	#talk = models.CharField(max_length = 200)

class Talk(models.Model):
	speaker = models.ForeignKey(Speaker)
	title = models.CharField(max_length= 100)
	description = models.TextField(max_length= 1000)
	category = models.CharField(max_length = 20)