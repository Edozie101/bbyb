from django.db import models

# Create your models here.

#import models from django.db 

#unlike RoR migrations are made directly from the models 

from django.db import models

#Property Model
class Property(models.Model):
	road = models.CharField(max_length = 250)
	town = models.CharField(max_length = 250)
	postcode = models.CharField(max_length = 10)
	description = models.CharField(max_length = 10000)
	features = models.CharField(max_length = 2000)
	pub_date = models.DateTimeField('date published')
	image = models.ImageField



# Stipe or Payment provider 




# User model


class User(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email= models.CharField(max_length = 100)
	postcode = models.CharField(max_length = 10)
	address = models.CharField(max_length = 400)
	password = models.CharField(max_length = 250)
	