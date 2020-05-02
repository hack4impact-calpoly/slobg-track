from .models import VolunteerRecord, Profile, ActivityChoice

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class NumberInput(forms.NumberInput):
    input_type = 'number'

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    # Profile Fields
    phone = forms.CharField(max_length=30, required=True, help_text='Required.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD', 
                                    widget=DateInput(attrs={'id':'dateTimePicker'}))
    medical_conditions = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':20}))
    areas_of_interest = forms.ModelMultipleChoiceField(queryset=ActivityChoice.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    volunteer_waiver_and_release = forms.CharField(max_length=50,required=True, help_text='Required.', label="Volunteer Waiver and Release Signature")
    esignature_date = birth_date

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 
        'phone','birth_date', 'medical_conditions', 'areas_of_interest', 
                'volunteer_waiver_and_release', 'esignature_date',)
        

class ProfileForm(forms.ModelForm):
    phone = forms.CharField(max_length=30, required=True, help_text='Required.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD', 
                                    widget=DateInput(attrs={'id':'dateTimePicker'}))
    medical_conditions = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':20}))
    areas_of_interest = forms.ModelMultipleChoiceField(queryset=ActivityChoice.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    volunteer_waiver_and_release = forms.CharField(max_length=50,required=True, help_text='Required.', label="Volunteer Waiver and Release Signature")
    esignature_date = birth_date
    class Meta:
        model = Profile
        fields = ('phone', 'birth_date', 'medical_conditions', 'areas_of_interest', 
                'volunteer_waiver_and_release', 'esignature_date',)
        widgets = {
          'medical_conditions': forms.Textarea(attrs={'rows':4, 'cols':20}),
        }

class VolunteerRecordForm(forms.ModelForm):
    class Meta:
        model = VolunteerRecord
        fields = ('activity', 'hours', 'date', 'supervisor')
        hours = forms.FloatField(min_value=0)
        widgets = {
            'date' : DateInput(attrs={'id':'dateTimePicker'}),
            'hours' : NumberInput(attrs={'id': 'form_hours', 'step': "0.25"})
        }


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
