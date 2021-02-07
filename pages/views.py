from django.shortcuts import render
from .models import BusinessInfo,Team
from cars.models import Car

# Cdef home(request):

def home(request):
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    teams = Team.objects.all()
    model_search = all_cars.values_list('model',flat=True).distinct()
    fuel_type_search = all_cars.values_list('fuel_type',flat=True).distinct()
    transmission_search = all_cars.values_list('transmission',flat=True).distinct()
    year_search = all_cars.values_list('year',flat=True).distinct()
    body_style_search = all_cars.values_list('body_style',flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'model_search':model_search,
        'fuel_type_search':fuel_type_search,
        'transmission_search':transmission_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
        }
    return render(request, 'pages/home.html', data)



def about(request):
    teams = Team.objects.all()
    return render(request, 'pages/about.html',{'teams': teams})


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')


def aboutBusiness(request):
    busines_info = BusinessInfo.objects.all()
    return render(request, 'templates/includes/main-nav.html', {'busines_info': busines_info})