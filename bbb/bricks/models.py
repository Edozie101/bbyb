import datetime
# Create your models here.

#import models from django.db 

#unlike RoR migrations are made directly from the models 

from django.db import models
from django.utils import timezone

#Property Model
class Property(models.Model):
	road = models.CharField(max_length = 250)
	town = models.CharField(max_length = 250)
	postcode = models.CharField(max_length = 10)
	description = models.CharField(max_length = 10000)
	features = models.CharField(max_length = 2000)
	pub_date = models.DateTimeField('date published')
	image = models.ImageField
	title = models.CharField(max_length = 250,default = "Property Title")
	expiry_date = models.DateTimeField


	def __str__(self):
		return self.title


	def was_published_less_than_a_day(self):
		return self.pub_date >= timzezone.now() - datetime.timedelta(days=1)

	def was_published_less_than_a_week(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)


	def expiring_in_less_than_a_week(self):
		return self.expiry_date - timezone.now() <= datetime.timedelta(days=7)


	def expiring_in_less_than_a_month(self):
		return self.expiry_date - timezone.now() <= datetime.timedelta(days=31)


	def expiring_in_less_than_a_year(self):
		return self.expiry_date - timezone.now() <= datetime.timedelta(days=365)


# Stipe or Payment provider 




# User model


class User(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email= models.CharField(max_length = 100)
	postcode = models.CharField(max_length = 10)
	address = models.CharField(max_length = 400)
	password = models.CharField(max_length = 250)


	def __str__(self):
		return self.first_name + self.last_name





# Favorites  add a many to many through favourites relationship
	


		