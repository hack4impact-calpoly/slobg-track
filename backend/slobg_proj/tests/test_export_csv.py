from django.test import TestCase
from slobg_app.models import VolunteerRecord
from slobg_app.views import export_csv
from slobg_app.forms import FilterForm
from django.utils import timezone


# Create your tests here.
# Test template based off of https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing


class VolunteerRecordModelTest(TestCase):
   @classmethod
   def setUpTestData(cls):
      print("Running VolunteerRecordModelTest...")
      # Set up non-modified objects used by all test methods

      # VolunteerRecord.objects.create(activity="Planting trees",
      #                      hours=2,
      #                      date=timezone.now(),
      #                      supervisor="Test Supervisor",
      #                      )
      # VolunteerRecord.objects.create(activity="Coding",
      #                      hours=4,
      #                      date=timezone.now(),
      #                      supervisor="Test Supervisor",
      #                      ) 

   def test_activity_form_valid(self):
      form = FilterForm(data={'start_date':'2020-02-27', 'end_date':'2020-02-28'})
      self.assertEquals(form.is_valid(), True)

   def test_activity_form_invalid_format(self):
      form = FilterForm(data={'start_date':'02-27-2020', 'end_date':'02-28-2020'})
      self.assertEquals(form.is_valid(), False)

   def test_activity_form_invalid_input(self):
      form = FilterForm(data={'start_date':'January 18th, 2020', 'end_date':'February 12th, 2020'})
      self.assertEquals(form.is_valid(), False)
   
   def test_activity_form_reversed_dates(self):
      form = FilterForm(data={'start_date':'2020-02-27', 'end_date':'2020-01-28'})
      self.assertEquals(form.is_valid(), False)

   def test_activity_form_reversed_years(self):
      form = FilterForm(data={'start_date':'2021-01-28', 'end_date':'2020-01-28'})
      self.assertEquals(form.is_valid(), False)

   def test_activity_form_reversed_months(self):
      form = FilterForm(data={'start_date':'2020-04-28', 'end_date':'2020-01-28'})
      self.assertEquals(form.is_valid(), False)

   def test_activity_form_reversed_days(self):
      form = FilterForm(data={'start_date':'2020-01-30', 'end_date':'2020-01-28'})
      self.assertEquals(form.is_valid(), False)
