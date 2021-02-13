from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

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
    contact.save()
    messages.success(request,"You request hase been submited")
    return redirect('/cars/'+car_id)
