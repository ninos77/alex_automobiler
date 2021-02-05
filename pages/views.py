from django.shortcuts import render
from .models import BusinessInfo

# Cdef home(request):

def home(request):
  return render(request, 'pages/home.html')



def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')


def aboutBusiness(request):
    busines_info = BusinessInfo.objects.all()
    return render(request, 'templates/includes/main-nav.html', {'busines_info': busines_info})