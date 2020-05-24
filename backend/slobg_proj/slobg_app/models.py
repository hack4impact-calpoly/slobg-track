from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


ACTIVITY_CHOICES = (('Maintenance', 'Maintenance'), 
					('Administration', 'Administration'), 
					('Outreach', 'Outreach'), 
					('Education', 'Education'),
					('Propagation', 'Propagation'),
					('Other', 'Other'))

class VolunteerRecord(models.Model):
	activity = models.CharField(max_length=256, blank=False, choices=ACTIVITY_CHOICES)
	hours = models.FloatField(blank=False)
	date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
	supervisor = models.CharField(max_length=256, blank=False)
	description = models.CharField(max_length=1000, blank=True, default='')
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


class ActivityChoice(models.Model):
	description = models.CharField(max_length=300)
	def __str__(self):
		return self.description

# Phone, email, birthdate, medical conditions, 
# interested areas to volunteer, waiver to sign


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=20, blank=True,
		help_text="Please enter your phone number in the following format: (XXX) XXX-XXXX")
	birth_date = models.DateField(null=True, blank=True)
	medical_conditions = models.TextField(max_length=512, blank=True,
		help_text="Please enter any medical conditions you may have. Write N/A if none.")
	areas_of_interest = models.ManyToManyField(ActivityChoice)
	photo_permission = models.BooleanField(blank=True, default=True)
	emergency_contact = models.CharField(blank=True, max_length=256)
	emergency_contact_phone_number = models.CharField(blank=True, max_length=256)
	volunteer_waiver_and_release = models.CharField(max_length=50, blank=True)
	esignature_date = models.DateTimeField(null=True, blank=True)
	
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
