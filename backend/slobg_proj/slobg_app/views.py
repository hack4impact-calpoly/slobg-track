from django.shortcuts import render

from .forms import VolunteerHoursForm
from .models import VolunteerHours

# Create your views here.
def home(request):
   user = request.user

   return render(request, 'slobg_app/home.html', {user: user})

def add_ind_hours_view(request):
   form = VolunteerHoursForm(request.POST or None)
   if form.is_valid():
      form.save()
      form = VolunteerHoursForm()
   
   context = {
      'form' : form
   }

   return render(request, "slobg_app/ind_add_hours.html", context)