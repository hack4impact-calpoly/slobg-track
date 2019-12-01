from .models import Volunteer, VolunteerHours
from django import forms

#Form for creating a new Volunteer model
#Form reflects the Individual Volunteer form on the SRS
class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'street_address', 'city', 'zipcode', 'state', 
                'phone', 'email', 'birthdate', 'work_preference', 
                'area_of_interest']


#class VolunteerForm(forms.ModelForm):
#    class Meta:
#        model = Volunteer
#        fields = ['username', 'name', 'street_address', 'city', 'zipcode', 
#                'state', 'phone', 'email', 'birthdate', 'work_preference', 
#                'area_of_interest']
#       widgets = {
#            'username' : forms.TextInput(
#                attrs={
#                    'class': 'form-control',
#                    'placeholder': 'username'
#                }),
#            'name' : forms.TextInput(
#                attrs={
#                    'class': 'form-control',
#                    'placeholder': 'First Last'
#                }),
#            'birthdate' : forms.TextInput(attrs={'class': 'form-control'})
#        }

class VolunteerHoursForm(forms.ModelForm):
    class Meta:
        model = VolunteerHours
        fields = ['date', 'hours', 'supervisor', 'activity']
        widgets = {
            'date':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'yyyy-mm-dd'
                }
            ),
            'hours':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'0'
                }
            ),
            'supervisor':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Supervisor Name'
                }
            ),
            'activity':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Describe the activity you volunteered for'
                }
            ),
        }

class GroupVolunteerForm(forms.ModelForm):
    class Meta:
        model = GroupVolunteerForm
        fields = ['activity','hours','date','supervisor',
        'number_volunteers','group_name','email']
        widgets = {
            'date':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'yyyy-mm-dd'
                }
            ),
            'hours':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'0'
                }
            ),
            'supervisor':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Supervisor Name'
                }
            ),
            'activity':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Describe the activity you volunteered for'
                }
            ),
            'number_volunteers':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'1'
                }
            ),
            'group_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Your group name here'
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':''
                }
            ),
        }
