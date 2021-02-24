from django.shortcuts import render,redirect
from .models import BusinessInfo,Team
from cars.models import Car,Model,Make
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator

# Cdef home(request):

def home(request):
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    all_models = Model.objects.all()
    all_makes = Make.objects.all()
    teams = Team.objects.all()
    paginator = Paginator(all_cars,3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    make_search = set(all_makes.values_list('make_name', flat=True))
    fuel_type_search = all_cars.values_list('fuel_type',flat=True).distinct()
    transmission_search = all_cars.values_list('transmission',flat=True).distinct()
    year_search = all_cars.values_list('year',flat=True).distinct()
    model_search = all_models.values_list('model_name',flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'paged_cars':paged_cars,
        'all_makes':all_makes,
        'fuel_type_search':fuel_type_search,
        'transmission_search':transmission_search,
        'year_search':year_search,
        'all_models':all_models,
        }
    return render(request, 'pages/home.html', data)



def about(request):
    teams = Team.objects.all()
    return render(request, 'pages/about.html',{'teams': teams})


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        email_subject = "You have Email from Alexautomobiler"
        message_body = 'Name: '+ name +'.'+'\nEmail: '+ email +'.'+'\n\n'+ message +'.'
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email 

        send_mail(

                email_subject,
                message_body,
                email,
                [admin_email],
                fail_silently=False,
                
            )
        messages.success(request,"You request hase been submited")
        return redirect('contact')     

    return render(request, 'pages/contact.html')


def aboutBusiness(request):
    busines_info = BusinessInfo.objects.all()
    return render(request, 'templates/includes/main-nav.html', {'busines_info': busines_info})