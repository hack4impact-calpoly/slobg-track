from .models import VolunteerForm, Volunteer

#Form for creating a new Volunteer model
#Form reflects the Individual Volunteer form on the SRS
class Volunteer(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'street_address', 'city', 'zipcode', 'state', 
                'phone', 'email', 'birthdate', 'work_preference', 
                'area_of_interest']

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = VolunteerForm
        fields = ['activity','hours','date']