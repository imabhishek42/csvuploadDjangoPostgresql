from django.db import models
from django import forms

# Create your models here.

class EventsForm(models.Model):

	id = models.AutoField (primary_key = True)
	name = models.TextField()
	phone = models.TextField()
	email = models.TextField()
	country = models.TextField()
	def __str__(self):
		return "Click on this : "+self.name

