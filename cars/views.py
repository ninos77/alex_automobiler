from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from .models import Car, Make, Model
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator
from django.contrib import messages

# Create your views here.

def cars(request):
  all_cars = Car.objects.order_by('-created_date')
  paginator = Paginator(all_cars,4)
  page = request.GET.get('page')
  paged_cars = paginator.get_page(page)
  data = {'all_cars':paged_cars}
  return render (request,'cars/cars.html',data)


def car_detail(request, id):
  singel_car = get_object_or_404(Car,pk=id)
  data = {'singel_car':singel_car}
  return render (request,'cars/car_detail.html',data)

def search(request):
  all_cars = Car.objects.order_by('-created_date')
  if 'keyword' in request.GET:
    keyword = request.GET['keyword']
    if not keyword:
       messages.error(request, "You didn't enter any search criteria!",)
       return redirect(reverse('cars'))
    if keyword:
      queries  = Q(description__icontains=keyword) | Q(make__make_name__iexact=keyword) | Q(transmission__iexact=keyword)| Q(fuel_type__iexact=keyword)| Q(model__model_name__iexact=keyword)
      all_cars = all_cars.filter(queries)
      return render (request,'cars/search.html',{'all_cars':all_cars})  

  if 'make' in request.GET:
    makes = request.GET['make']
    if makes:
      all_cars  = all_cars.filter(make__make_name__iexact=makes)
  data = {'all_cars':all_cars}
  return render (request,'cars/search.html',data)  

