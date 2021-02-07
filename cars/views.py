from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger, Paginator

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
    if keyword:
      queries  = Q(description__icontains=keyword) | Q(make__icontains=keyword) | Q(transmission__icontains=keyword)| Q(fuel_type__icontains=keyword)| Q(model__icontains=keyword)
      all_cars = all_cars.filter(queries)


  if 'make' in request.GET:
    make = request.GET['make']
    if make:
      queries  = Q(make__iexact=make)
      all_cars = all_cars.filter(queries) 
  if 'fuel_type' in request.GET:
    fuel_type = request.GET['fuel_type']
    if fuel_type:
      queries  = Q(fuel_type__iexact=fuel_type)
      all_cars = all_cars.filter(queries)

  if 'year' in request.GET:
    year = request.GET['year']
    if year:
      queries  = Q(year__iexact=year)
      all_cars = all_cars.filter(queries)    
  
  if 'transmission' in request.GET:
    transmission = request.GET['transmission']
    if transmission:
      queries  = Q(transmission__iexact=transmission)
      all_cars = all_cars.filter(queries)

  if 'body_style' in request.GET:
    body_style = request.GET['body_style']
    if body_style:
      queries  = Q(body_style__iexact=body_style)
      all_cars = all_cars.filter(queries)

                
  data = {'all_cars':all_cars}
  return render (request,'cars/search.html',data)  

