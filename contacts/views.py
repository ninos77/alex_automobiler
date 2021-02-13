from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.

def inquiry(request):
  if request.method == 'POST':
    full_name = request.POST['full_name']
    car_id = request.POST['car_id']
    email = request.POST['email']
    customer_need = request.POST['customer_need']
    car_title = request.POST['car_title']
    message = request.POST['message']
    has_contact = Contact.objects.all().filter(email=email,car_id=car_id)
    if has_contact:
      messages.error(request,'Du har allerede spurgt om denne bil')
      return redirect('/cars/'+car_id)
    
    contact = Contact(full_name=full_name,email=email,customer_need=customer_need,car_title=car_title,message=message,car_id=car_id)

    admin_info = User.objects.get(is_superuser=True)
    admin_email = admin_info.email 

    send_mail(

          'Aske about a car',
          'You have message abour this car '+ car_title ,
          email,
          [admin_email],
          fail_silently=False,
          
        )


    contact.save()
    messages.success(request,"You request hase been submited")
    return redirect('/cars/'+car_id)
