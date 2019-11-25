from django.shortcuts import render

# Create your views here.
def home(request):
   user = request.user

   return render(request, 'slobg_app/home.html', {user: user})