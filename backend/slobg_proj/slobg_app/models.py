from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


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
	volunteer_waiver_and_release = models.CharField(max_length=50, blank=True, 
		help_text="""San Luis Obispo Botanical Garden (SLOBG) is not responsible for 
		an injury or accident that may occur during my participation as a volunteer in 
		any activity or event. I understand that by signing below I assume full responsibility
		for any injury or accident that may occur during my participation as a volunteer, and 
		I hereby release and hold harmless and covenant not to file suit against SLOBG, 
		employees and any affiliated individuals (“releasees”) associated with my 
		participation from any loss, liability or claims I may have arising out of my 
		participation, including personal injury or damage suffered by me or others, whether 
		caused by falls, contact with participants, conditions of the facility, negligence of 
		the releasees or otherwise. If I do not agree to these terms, I understand that I am 
		not allowed to participate in the volunteer program. Please enter your full name below, 
		verifying you have read the waiver.""")
	esignature_date = models.DateTimeField(null=True, blank=True)
	
	# fields for admin only
	was_interviewed = models.BooleanField(null=True)
	follow_up_email = models.BooleanField(null=True)
	distribution_list = models.BooleanField(null=True)
	background_check = models.BooleanField(null=True)
	harassment_training = models.BooleanField(null=True)
	first_aid_cpr = models.BooleanField(null=True)
	emergency_contact = models.TextField(max_length=100, blank=True)
	emergency_contact_relationship = models.TextField(max_length=100, blank=True)
	emergency_contact_phone_number = models.TextField(max_length=100, blank=True)

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
