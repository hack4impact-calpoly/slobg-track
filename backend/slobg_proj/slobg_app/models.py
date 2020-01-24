from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
'''
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	total_volunteer_hours = models.FloatField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Volunteer(models.Model):
	WORK_PREFERENCES = [
		("work_alone", "Work Alone"),
		("work_in_groups", "Work in Groups"),
	]
	AREAS_OF_INTEREST = []
	total_hours = models.FloatField(default=0)
	email = models.EmailField(max_length=254)
	username = models.CharField(max_length=200, default="")
	name = models.CharField(max_length=200, default="")
	street_address = models.CharField(max_length=200, default="")
	city = models.CharField(max_length=200, default="")
	zipcode = models.CharField(max_length=200, default="")
	state = models.CharField(max_length=200, default="")
	phone = models.CharField(max_length=100, default="")
	birthdate = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
	work_preference = models.CharField(max_length=14, choices=WORK_PREFERENCES, default="work_alone")
	area_of_interest = models.CharField(max_length=200, choices=AREAS_OF_INTEREST, default="")
	
	def __str__(self):
		return "Username: {}, Email: {}".format(self.username, self.email)

class VolunteerHours(models.Model):
	activity = models.CharField(max_length=256, blank=False)
	hours = models.FloatField(blank=False)
	date = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
	supervisor = models.CharField(max_length=256, blank=False)

class GroupVolunteerModel(models.Model):
	activity = models.CharField(max_length=256, blank=False)
	hours = models.FloatField(blank=False)
	date = models.DateTimeField(default=djnow)
	supervisor = models.EmailField(max_length=254)
	number_volunteers = models.IntegerField()
	group_name = models.CharField(max_length=200, default="")
	email = models.EmailField(max_length=254)

'''