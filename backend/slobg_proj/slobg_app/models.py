from django.db import models

# Create your models here.

class Volunteer(models.Model):
	total_hours = models.FloatField()
	email = models.EmailField(max_length=254)
	username = models.CharField(max_length=200)

	def __str__(self):
		return "Username: {}, Email: {}".format(self.username, self.email)
