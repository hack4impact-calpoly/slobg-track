from django.test import TestCase
from slobg_app.models import VolunteerRecord
from django.utils import timezone


# Create your tests here.
# Test template based off of https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing


class VolunteerRecordModelTest(TestCase):
   @classmethod
   def setUpTestData(cls):
      print("Running VolunteerRecordModelTest...")
      # Set up non-modified objects used by all test methods
      VolunteerRecord.objects.create(activity="Planting trees",
                           hours=2,
                           date=timezone.now(),
                           supervisor="Test Supervisor",
                           )

   def test_activity_label(self):
      rec = VolunteerRecord.objects.get(id=1)
      field_label = rec._meta.get_field('activity').verbose_name
      self.assertEquals(field_label, 'activity')

   def test_supervisor_label(self):
      rec = VolunteerRecord.objects.get(id=1)
      field_label = rec._meta.get_field('supervisor').verbose_name
      self.assertEquals(field_label, 'supervisor')

   def test_activity_max_length(self):
      rec = VolunteerRecord.objects.get(id=1)
      max_length = rec._meta.get_field('activity').max_length
      self.assertEquals(max_length, 256)

   def test_object_name_formatting(self):
      rec = VolunteerRecord.objects.get(id=1)
      expected_object_name = "Owner: {}, Date: {}, Activity: {}".format(
         rec.owner, rec.date, rec.activity)
      self.assertEquals(expected_object_name, str(rec))