from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ACTIVITY_CHOICES = (('Maintenance', 'Maintenance'), 
					('Administration', 'Administration'), 
					('Outreach', 'Outreach'), 
					('Education', 'Education'))

class VolunteerRecord(models.Model):
	activity = models.CharField(max_length=256, blank=False, choices=ACTIVITY_CHOICES)
	hours = models.FloatField(blank=False)
	date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
	supervisor = models.CharField(max_length=256, blank=False)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return "Owner: {}, Date: {}, Activity: {}".format(self.owner, self.date, self.activity)
	

class GroupVolunteerModel(models.Model):
	activity = models.CharField(max_length=256, blank=False)
	hours = models.FloatField(blank=False)
	date = models.DateTimeField(blank=False)
	supervisor = models.EmailField(max_length=254)
	number_volunteers = models.IntegerField()
	group_name = models.CharField(max_length=200, default="")
	email = models.EmailField(max_length=254)
