from django.utils import timezone
from slobg_app.forms import FilterForm
from slobg_app.forms import *
from django.test import Client
from django.test import TestCase

class VolunteerRecordFormTest(TestCase):
    def test_valid_Volunteer(self):
        form = VolunteerRecordForm(data ={'activity': "planting", 'hours':5, 'date':"05/09/2020", 'supervisor':"Joscelyn"})
        self.assertTrue(form.is_valid())
        self.assertTrue(form.data['activity'] == "planting")
        self.assertTrue(form.data['activity'] == "planting")
        self.assertTrue(form.data['activity'] == "planting")
        self.assertTrue(form.data['activity'] == "planting")

class FilterFormTest(TestCase):
    def test_start_date(self):
        form = FilterForm()
        self.assertTrue(form.fields['start_date'].label == None or form.fields['start_date'] == 'start_date')

    def test_end_date(self):
        form = FilterForm()
        self.assertTrue(form.fields['end_date'].label == None or form.fields['end_date'] == 'end_date')
