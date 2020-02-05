from django.shortcuts import render, redirect

from .forms import SignUpForm, VolunteerRecordForm
from .models import VolunteerRecord
# Signup/Login stuff
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Csv stuff
from django.http import HttpResponse
import csv

#Export to csv function
def export_csv(request):
   response = HttpResponse(content_type='text/csv')
   response['Content-Disposition'] = 'attachment; filename="volunteer_history.csv"'

   writer = csv.writer(response)
   writer.writerow(['Volunteer', 'Date', 'Hours', 'Description', 'Supervisor'])

   if(request.user.is_superuser):
      records = VolunteerRecord.objects.all()
   else:
      records = VolunteerRecord.objects.filter(owner=request.user)

   for record in records:
      volunteer = record.owner.first_name + ' ' + record.owner.last_name
      date = record.date
      hours = record.hours
      desc = record.activity
      supervisor = record.supervisor

      writer.writerow((volunteer, date, hours, desc, supervisor))

   return response

def landing(request):
   return render(request, 'landing.html')

def signup(request):
   if request.method == "POST":
      form = SignUpForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=username, password=raw_password)
         login(request, user)
         return redirect('/add_individual_hours')
      else:
         print("form not valid")
   else:
      form = SignUpForm()
   return render(request, "signup.html", {"form":form})


@login_required
def home(request):
   user = request.user
   return redirect('/add_individual_hours')

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
         return redirect('/success')
      else:
         print("form not valid")
   else:
      form = VolunteerRecordForm()

   return render(request, "add_individual_hours.html", {"form": form})



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
   return render(request, "history.html", {"records" : records})