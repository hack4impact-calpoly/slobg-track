from django.forms import ModelForm
from slobg_app.models import Volunteer

#Form for creating a new Volunteer model
#Form reflects the Individual Volunteer form on the SRS
class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'street_address', 'city', 'zipcode', 'state', 
                'phone', 'email', 'birthdate', 'work_preference', 
                'area_of_interest']