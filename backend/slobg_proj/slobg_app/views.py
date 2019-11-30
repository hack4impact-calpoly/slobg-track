from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import GroupVolunteerForm

# Create your views here.
def home(request):
   user = request.user

   return render(request, 'slobg_app/home.html', {user: user})

def group_volunteer(request):
   if request.method == 'POST':
      form = GroupVolunteerForm(request.POST)
      if form.is_valid():
         return HttpResponseRedirect('/home')

   return render(request, 'slobg_app/group_sign_in.html', {})