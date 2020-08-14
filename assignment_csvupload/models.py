from django.db import models

# Create your models here.

class EventsForm(models.Model):

    name = models.TextField()

    phone = models.TextField()

    email = models.TextField()

    country = models.TextField()

    id = models.AutoField (primary_key = True)

    def is_valid(self):
    	return 1
    def __str__(self):
        return self.name
