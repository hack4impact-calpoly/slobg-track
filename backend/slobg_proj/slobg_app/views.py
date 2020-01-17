from django.shortcuts import render, redirect, render_to_response

from .forms import SignUpForm, VolunteerRecordForm

# Signup/Login stuff
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def signup(request):
   if request.method == "POST":
      form = SignUpForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=username, password=raw_password)
         login(request, user)
         return redirect('/')
      else:
         print("form not valid")
   else:
      form = SignUpForm()
   return render(request, "signup.html", {"form":form})


@login_required
def home(request):
   user = request.user
   return render(request, 'home.html', {user: user})

@login_required
def add_individual_hours(request):
   form = VolunteerRecordForm(request.POST)
   if form.is_valid():
      form.save()
      return redirect('/')
   context = {
      'form' : form
   }
   return render(request, "ind_add_hours.html", context)

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
