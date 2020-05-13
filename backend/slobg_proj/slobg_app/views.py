from django.shortcuts import render, redirect

from .forms import SignUpForm, ProfileForm, VolunteerRecordForm, FilterForm
from .models import VolunteerRecord, ActivityChoice
from django.conf import settings
# Signup/Login stuff
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Csv stuff
from django.http import HttpResponse
import csv
from django.db.models import Sum
from django.contrib.auth.models import User


# Email Receipt Stuff
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


#Export to csv function
def export_csv(request, start_date, end_date):
   response = HttpResponse(content_type='text/csv')
   response['Content-Disposition'] = 'attachment; filename="volunteer_history: {} to {}.csv"'.format(start_date, end_date)

   writer = csv.writer(response)
   writer.writerow(['Volunteer', 'Date', 'Hours', 'Description', 'Supervisor'])

   if(request.user.is_superuser):
      records = VolunteerRecord.objects.all().filter(date__range=[start_date, end_date])
   else:
      records = VolunteerRecord.objects.filter(owner=request.user, date__range=[start_date, end_date])

   for record in records:
      volunteer = record.owner.first_name + ' ' + record.owner.last_name
      date = record.date
      hours = record.hours
      desc = record.activity
      supervisor = record.supervisor

      writer.writerow((volunteer, date, hours, desc, supervisor))
   
   return response

@login_required
def export(request):
   if request.method == "POST":
      form = FilterForm(request.POST)
      if form.is_valid():
         start = form.cleaned_data['start_date']
         end = form.cleaned_data['end_date']
         response = export_csv(request, start, end)
         return response
      else:
         print("form not valid")
   else:
      form = FilterForm()
   return render(request, 'export.html', {'form':form})

@login_required
def export_contact(request):
   if request.method == "POST":
      form = FilterForm(request.POST)
      if form.is_valid():
         start = form.cleaned_data['start_date']
         end = form.cleaned_data['end_date']
         response = export_contacts(request, start, end)
         return response
      else:
         print("form not valid")
   else:
      form = FilterForm()
   return render(request, 'export_contact.html', {'form':form})

def export_contacts(request, start_date, end_date):
   print(request)
   response = HttpResponse(content_type='text/csv')
   response['Content-Disposition'] = 'attachment; filename="volunteer_contacts: {} to {}.csv"'.format(start_date, end_date)

   writer = csv.writer(response)
   writer.writerow(['emails'])

   if(request.user.is_superuser):
      users = User.objects.all().filter(date_joined__range=[start_date, end_date])
   else:
      users = User.objects.filter(owner=request.user, date_joined__range=[start_date, end_date])

   for user in users:
      writer.writerow([user.email])
   
   return response



   
def landing(request):
   return render(request, 'landing.html')

def signup(request):
   if request.method == "POST":
      form = SignUpForm(request.POST)
      if form.is_valid():
         user = form.save()
         user.refresh_from_db() 
         #load profile
         user.profile.phone = form.cleaned_data.get('phone')
         user.profile.birth_date = form.cleaned_data.get('birth_date')
         user.profile.medical_conditions = form.cleaned_data.get('medical_conditions')
         areas_of_interest = form.cleaned_data.get('areas_of_interest')
         # ActivityChoice.objects.create()
         user.profile.areas_of_interest.add(*areas_of_interest)
         user.profile.volunteer_waiver_and_release = form.cleaned_data.get('volunteer_waiver_and_release')
         user.profile.esignature_date = form.cleaned_data.get('esignature_date')
         user.save()
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=user.username, password=raw_password)
         login(request, user)
         return redirect('/add_individual_hours')
      else:
         print("form not valid")
   else:
      form = SignUpForm()
   return render(request, "signup.html", {
         "user_form" : form,
      })


@login_required
def home(request):
   return redirect('add_individual_hours')

@login_required
def success(request):
    return render(request, "success.html")

@login_required
def add_individual_hours(request):
   if request.method == "POST":
      form = VolunteerRecordForm(request.POST)
      if form.is_valid():
            # Set user field in the form here
            print("before commit false")
            record = form.save(commit = False)
            print("after", record)
            record.owner = request.user
            record.save()
            print("success")
            subject = 'SLO Botanical Garden - Tracking Form Receipt'
            html_message = render_to_string('email_template.html', {'form': form.cleaned_data}) 
            plain_message = strip_tags(html_message)
            from_email = settings.DEFAULT_FROM_EMAIL
            to = request.user.email
            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
            return redirect('/success')
      else:
         print("form not valid")
   else:
      form = VolunteerRecordForm()

   return render(request, "add_individual_hours.html", {"form": form, "user": request.user})



# @login_required
# def add_group_hours(request):
#    form = GroupVolunteerForm(request.POST or None)
#    if form.is_valid():
#       form = GroupVolunteerForm()
#       form.save()
#    context = {
#       'form': form
#    }
#    return render(request, 'group_sign_in.html', {})

@login_required
def history(request):
   current_user = request.user
   if current_user.is_staff:
      records = VolunteerRecord.objects.all()
   else:
      records = VolunteerRecord.objects.filter(owner = current_user)
   running_total = sum(rec.hours for rec in records)
   if records.count() > 10:
      records = records[records.count() - 10:]
   records = list(records)
   records.sort(key=lambda rec: rec.date, reverse=True)
   return render(request, "history.html", {"records" : records, "running_total":running_total})


@login_required
def profile(request):
   current_user = request.user
   profile_form = ProfileForm(instance=request.user.profile)
   hours = VolunteerRecord.objects.filter(
      owner = current_user).all().aggregate(
         total_hours=Sum('hours'))['total_hours'] or 0
   return render(request, "profile.html", {'hours' : hours, 'user': current_user, 'profile_form': profile_form})

@login_required
def update_profile(request):
   if request.method == "POST":
      user_form = SignUpForm(request.POST, instance=request.user)
      profile_form = ProfileForm(request.POST, instance=request.user.profile)
      if user_form.is_valid() and profile_form.is_valid():
         user_form.save()
         profile_form.save()
         print("Profile successfully updated.")
         return redirect('/profile')
      else:
         print("user_form or profile_form not valid.")
   else:
        user_form = SignUpForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
   return render(request, 'update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
