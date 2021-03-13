from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('finance', views.finance, name='finance'),
    path('contact', views.contact, name='contact'),
    


]