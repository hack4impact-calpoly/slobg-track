from django.shortcuts import render, redirect

from .forms import SignUpForm, VolunteerRecordForm
from .models import VolunteerRecord
# Signup/Login stuff
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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
         return redirect('/')
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
   records = VolunteerRecord.objects.filter(owner = current_user)   # fix filter by user
   return render(request, "history.html", {"records" : records})