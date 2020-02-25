from django.shortcuts import render, redirect

from .forms import SignUpForm, VolunteerRecordForm, FilterForm
from .models import VolunteerRecord
from django.conf import settings
# Signup/Login stuff
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Csv stuff
from django.http import HttpResponse
import csv

# Email Receipt Stuff
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


#Export to csv function
def export_csv(request, start_date, end_date):
   response = HttpResponse(content_type='text/csv')
   response['Content-Disposition'] = 'attachment; filename="volunteer_history: {} to {}.csv"'.format(start_date, end_date)
   print(start_date)
   print(end_date)
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
<<<<<<< HEAD
         export_csv(request, start, end)
=======
         response = export_csv(request, start, end)
         return response
>>>>>>> 258fe40924d2645afa4fce732d379f1e735629d0
      else:
         print("form not valid")
   else:
      form = FilterForm()
   return render(request, 'export.html', {'form':form})


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