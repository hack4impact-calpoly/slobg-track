from django.test import Client, TestCase
from django.urls import resolve
from django.urls import reverse

class HomePageTest(TestCase):
    def test_root_url_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.view_name, 'home')

    def test_logged_user_home(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_redirect_home_to_add_individal_hours(self):
        response = self.client.get('/add_individual_hours/', follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)

    def test_redirect_home_to_history(self):
        response = self.client.get('/history/', follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)

    # def test_redirect_home_to_profile(self):
    #     response = self.client.get('/profile/', follow=True)
    #     self.assertEqual(response.redirect_chain[0][1], 302)

class LandingPageTest(TestCase):
    def test_landing_url_to_landing_page_view(self):
        found = resolve('/landing/')
        self.assertEqual(found.view_name, 'landing')

    def test_logged_user_landing(self):
        response = self.client.get('/landing/', follow=True)
        self.assertEqual(response.status_code, 200)

class AddIndividualHoursPageTest(TestCase):
    def test_add_individual_hours_url_to_add_individual_hours_page_view(self):
        found = resolve('/add_individual_hours/')
        self.assertEqual(found.view_name, 'add_individual_hours')

    def test_logged_user_add_individual_hours(self):
        response = self.client.get('/add_individual_hours/', follow=True)
        self.assertEqual(response.status_code, 200)

class HistoryPageTest(TestCase):
    def test_history_url_to_hisory_page_view(self):
        found = resolve('/history/')
        self.assertEqual(found.view_name, 'history')

    def test_logged_user_history(self):
        response = self.client.get('/history/', follow=True)
        self.assertEqual(response.status_code, 200)

class ExportPageTest(TestCase):
    def test_export_url_to_export_page_view(self):
        found = resolve('/export/')
        self.assertEqual(found.view_name, 'export')

    def test_logged_user_export(self):
        response = self.client.get('/export/', follow=True)
        self.assertEqual(response.status_code, 200)

# class Export_CSVPageTest(TestCase):
#     def test_export_csv_url_to_export_csv_page_view(self):
#         found = resolve('/export/')
#         self.assertEqual(found.view_name, 'export_csv')

class SuccessPageTest(TestCase):
    def test_success_url_to_success_page_view(self):
        found = resolve('/success/')
        self.assertEqual(found.view_name, 'success')

    def test_logged_user_success(self):
        response = self.client.get('/success/', follow=True)
        self.assertEqual(response.status_code, 200)