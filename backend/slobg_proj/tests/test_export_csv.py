from django.test import TestCase, RequestFactory
from slobg_app.models import VolunteerRecord
from slobg_app.views import export_csv
from slobg_app.forms import FilterForm
from django.utils import timezone
from django.http import HttpRequest
from django.contrib.auth.models import User



# Create your tests here.
# Test template based off of https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing


class ExportCSVTest(TestCase):

   def setUp(self):
      self.factory = RequestFactory()
      self.user = User.objects.create_user(
            username='admin', email='admin@gmail.com', password='pass', first_name='Test', last_name='Admin')
      self.jp = User.objects.create_user(username='jp', email='jpoist97@gmail.com', password='pass', first_name='J', last_name='Admin')
      
      VolunteerRecord.objects.create(activity="Planting trees",
                           hours=2,
                           date='2020-02-27',
                           supervisor="Test Supervisor",
                           owner = self.user
                           )
      VolunteerRecord.objects.create(activity="Coding",
                           hours=4,
                           date='2020-03-27',
                           supervisor="Test Supervisor",
                           owner = self.user
                           )
      VolunteerRecord.objects.create(activity="Testing",
                           hours=3,
                           date='2020-02-28',
                           supervisor="Test Supervisor",
                           owner = self.user
                           ) 
      VolunteerRecord.objects.create(activity="Testing",
                           hours=3,
                           date='2020-02-28',
                           supervisor="Test Supervisor",
                           owner = self.jp
                           )   

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


   def test_export_csv_normal_input(self):
      request = self.factory.post('/export/')
      request.user = self.user
      response = export_csv(request, '2020-02-27', '2020-03-28')
      split_response = response.content.decode('utf-8').rstrip().split('\n')

      for i in range(0, len(split_response)):
         split_response[i] = split_response[i].split(',')

      self.assertEquals(len(split_response), 4)

      self.assertEquals(split_response[0][0], 'Volunteer')
      self.assertEquals(split_response[0][1], 'Date')
      self.assertEquals(split_response[0][2], 'Hours')
      self.assertEquals(split_response[0][3], 'Description')


   def test_export_csv_same_date(self):
      request = self.factory.post('/export/')
      request.user = self.user
      response = export_csv(request, '2020-02-27', '2020-02-27')
      split_response = response.content.decode('utf-8').rstrip().split('\n')

      for i in range(0, len(split_response)):
         split_response[i] = split_response[i].split(',')

      self.assertEquals(len(split_response), 2)

      self.assertEquals(split_response[0][0], 'Volunteer')
      self.assertEquals(split_response[0][1], 'Date')
      self.assertEquals(split_response[0][2], 'Hours')
      self.assertEquals(split_response[0][3], 'Description')

      self.assertEquals(split_response[1][1], '2020-02-27')


   def test_export_csv_same_date_jp(self):
      request = self.factory.post('/export/')
      request.user = self.jp
      response = export_csv(request, '2020-02-28', '2020-02-28')
      split_response = response.content.decode('utf-8').rstrip().split('\n')

      for i in range(0, len(split_response)):
         split_response[i] = split_response[i].split(',')

      self.assertEquals(len(split_response), 2)

      self.assertEquals(split_response[0][0], 'Volunteer')
      self.assertEquals(split_response[0][1], 'Date')
      self.assertEquals(split_response[0][2], 'Hours')
      self.assertEquals(split_response[0][3], 'Description')

      self.assertEquals(split_response[1][1], '2020-02-28')
