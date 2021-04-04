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
  all_makes = Make.objects.all()
  car_account = Car.objects.all().count()   
  paginator = Paginator(all_cars,6)
  page = request.GET.get('page')
  paged_cars = paginator.get_page(page)
  data = {'paged_cars':paged_cars,'all_makes':all_makes,'cars':all_cars,'car_acount':car_account}
  return render (request,'cars/cars.html',data)


def car_detail(request, id):
  singel_car = get_object_or_404(Car,pk=id)
  data = {'singel_car':singel_car}
  return render (request,'cars/car_detail.html',data)

def search(request):
  make = None
  model = None
  min_price = None
  keyword = None
  all_cars = Car.objects.order_by('-created_date')
  all_makes = Make.objects.all()
  if 'keyword' in request.GET:
    keyword = request.GET['keyword']
    if keyword:
      queries  = Q(description__icontains=keyword) | Q(make__make_name__iexact=keyword) | Q(transmission__iexact=keyword)| Q(fuel_type__iexact=keyword)| Q(model__model_name__iexact=keyword)
      all_cars = all_cars.filter(queries)

  if 'make' in request.GET:
    make = request.GET['make']
    if make:
      all_cars  = all_cars.filter(make_id=make) 

  if 'min_price' and 'max_price'  in request.GET:
    min_price = request.GET['min_price']
    max_price = request.GET['max_price']
    if min_price == 0 and max_price == 500000 and make==None and model==None and keyword==None:
      messages.error(request, "You didn't enter any search criteria!")
      return redirect(reverse('cars')) 

    all_cars = all_cars.filter(price__gte=min_price,price__lte=max_price) 
  if min_price == 0 and max_price == 500000 and not keyword and not make and not model and not min_price:
    messages.error(request, "You didn't enter any search criteria!")
    return redirect(reverse('cars')) 
  context ={

    'all_cars':all_cars,
    'all_makes':all_makes
  }
  return render (request,'cars/search.html',context) 


