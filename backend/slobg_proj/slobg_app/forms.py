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
    class Meta:
        model = VolunteerRecord
        fields = ('activity', 'hours', 'date', 'supervisor')
        widgets = {'date' : DateInput(attrs={'id':'dateTimePicker'})}


class FilterForm(forms.Form):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)


    def is_valid(self):

        valid = super(FilterForm, self).is_valid()
        if not valid:
            return valid


        start_year = self.cleaned_data['start_date'].year
        start_month = self.cleaned_data['start_date'].month
        start_day = self.cleaned_data['start_date'].day

        end_year = self.cleaned_data['end_date'].year
        end_month = self.cleaned_data['end_date'].month
        end_day = self.cleaned_data['end_date'].day

        if(start_year < end_year):
            return True
        elif(start_year > end_year):
            return False
        
        if(start_month < end_month):
            return True
        elif(start_month > end_month):
            return False

        if(start_day <= end_day):
            return True

        return False
