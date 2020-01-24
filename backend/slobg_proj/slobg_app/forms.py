from .models import VolunteerRecord

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class DateInput(forms.DateInput):
    input_type = 'date'

class VolunteerRecordForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        # Update user hours here once User model is extended.
        super(VolunteerRecordForm, self).save(*args, **kwargs)

    class Meta:
        model = VolunteerRecord
        fields = ('activity', 'hours', 'date', 'supervisor')
        widgets = {'date' : DateInput(attrs={'id':'dateTimePicker'})}

''' 
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
        model = GroupVolunteerModel
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
'''