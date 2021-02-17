from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField

# Create your models here.

class Make(models.Model):
  make_name = models.CharField(max_length=100,verbose_name='bilproducenter')

  def __str__(self):
    return self.make_name

class Model(models.Model):
  model_name = models.CharField(max_length=100,verbose_name='model')
  make = models.ForeignKey("Make",null=True, blank=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.model_name


class Style(models.Model):
  style_name = models.CharField(max_length=100,verbose_name='bil kaross stil') 

  def __str__(self):
    return self.style_name


class Car(models.Model):
   year_choice = []
   for r in range(1980,(datetime.now().year+1)):
     year_choice.append((r,r))

   features_choices = (
        ('Bakkamera', 'Bakkamera'),
        ('Fartpilot, manuel', 'Fartpilot, manuel'),
        ('Fartpilot, adaptiv', 'Fartpilot, adaptiv'),
        ('Fjernlys assistent', 'Fjernlys assistent'),
        ('Kurvelys', 'Kurvelys'),
        ('Vognbaneassistent', 'Vognbaneassistent'),
        ('Alufælge', 'Alufælge'),
        ('Anhængertræk, fast', 'Anhængertræk, fast'),
        ('Anhængertræk, aftageligt', 'Anhængertræk, aftageligt'),
        ('LED forlygter', 'LED forlygter'),
        ('Soltag, manuelt', 'Soltag, manuelt'),
        ('Soltag, elektrisk', 'Soltag, elektrisk'),
        ('Panoramatag', 'Panoramatag'),
        ('Xenonlygter', 'Xenonlygter'),
        ('Android auto', 'Android auto'),
        ('Apple carplay', 'Apple carplay'),
        ('Elruder', 'Elruder'),
        ('Gear, manuel', 'Gear, manuel'),
        ('Headup display', 'Headup display'),
        ('Navigation', 'Navigation'),
        ('Nøglefri betjening', 'Nøglefri betjening'),
        ('Varme i sæder', 'Varme i sæder'),
        ('Varme, aircondition', 'Varme, aircondition'),
        ('Varme, klimaanlæg', 'Varme, klimaanlæg'),
    )

   door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )  

   fuel_choices = (
        ('Bensin', 'Bensin'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('EL', 'EL'),
        ('Ethanol', 'Ethanol'),

    )

   transmission_choices =(
    ('Automatisk ','Automatisk'),
    ('Manuel','Manuel'),
    ) 


   car_title = models.CharField(max_length=255,verbose_name='Biltitel')
   address = models.CharField(max_length=100,verbose_name='adresse')
   color = models.CharField(max_length=100,verbose_name='farve')
   make  = models.ForeignKey(Make,null=True, blank=True, on_delete=models.SET_NULL,verbose_name='bilmærke',related_name='make') 
   model = models.ForeignKey(Model,null=True, blank=True, on_delete=models.SET_NULL,verbose_name='model',related_name='model')                              
   year = models.IntegerField(('år'), choices=year_choice[::-1])
   condition = models.CharField(max_length=100,null=True,blank=True,verbose_name='tilstand')
   price= models.DecimalField(max_digits=10, decimal_places=2,verbose_name='pris')
   reduced_price= models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,verbose_name='nedsat pris')
   description = RichTextField(verbose_name='beskrivelse')
   car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
   car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   car_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   features = MultiSelectField(choices=features_choices,verbose_name='funktioner')
   body_style = models.ForeignKey("Style",null=True, blank=True, on_delete=models.SET_NULL,verbose_name='bil kaross stil') 
   transmission = models.CharField(choices=transmission_choices, max_length=25,verbose_name='gear')
   km = models.IntegerField()
   vehicle_number = models.CharField(null=True, blank=True, max_length=25,verbose_name='nummerplade')
   doors = models.CharField(choices=door_choices, max_length=10,verbose_name='døre')
   fuel_type = models.CharField(choices=fuel_choices, max_length=10,verbose_name='brændstoftype')
   is_featured = models.BooleanField(default=False,verbose_name='er vist')
   is_sold = models.BooleanField(default=False,verbose_name='sælges')
   created_date = models.DateTimeField(default=datetime.now, blank=True)


   def __str__(self):
      return self.car_title



   def car_count(self):
     return self.objects.all().count()   

