from django.db import models
from datetime import date

# Create your models here.

class Volunteer(models.Model):
	WORK_PREFERENCES = [
		("work_alone", "Work Alone"),
		("work_in_groups", "Work in Groups"),
	]
	AREAS_OF_INTEREST = []

	total_hours = models.FloatField()
	email = models.EmailField(max_length=254)
	username = models.CharField(max_length=200, default="")
	name = models.CharField(max_length=200, default="")
	street_address = models.CharField(max_length=200, default="")
	city = models.CharField(max_length=200, default="")
	zipcode = models.CharField(max_length=200, default="")
	state = models.CharField(max_length=200, default="")
	phone = models.CharField(max_length=100, default="")
	birthdate = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
	work_preference = models.CharField(max_length=1, choices=WORK_PREFERENCES, default="work_alone")
	area_of_interest = models.CharField(max_length=200, choices=AREAS_OF_INTEREST, default="")
	
	def __str__(self):
		return "Username: {}, Email: {}".format(self.username, self.email)
