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

  ('aut.','aut.'),

  ('aut.gear/tiptronic','aut.gear/tiptronic'),

  ('alu.','alu'),

  ('15" Alufælge','15" Alufælge'),

  ('16" Alufælge','16" Alufælge'),

  ('17" Alufælge','17" Alufælge'),

  ('18" Alufælge','18" Alufælge'),

  ('19" Alufælge','19" Alufælge'),

  ('20" Alufælge','20" Alufælge'),

  ('21" Alufælge','21" Alufælge'),

  ('22" Alufælge','22" Alufælge'),

  ('vinterhjul','vinterhjul'),

  ('varme i rat','varme i rat'),

  ('airc.','airc.'),

  ('fuldaut. klima','fuldaut. klima'),

  ('2 zone klima','2 zone klima'),

  ('3 zone klima','3 zone klima'),

  ('4 zone klima','4 zone klima'),

  ('køl i handskerum','køl i handskerum'),

  ('elektrisk kabinevarmer','elektrisk kabinevarmer'),

  ('motorkabinevarmer','motorkabinevarmer'),

  ('alarm','alarm'),

  ('c.lås','c.lås'),

  ('fjernb. c.lås','fjernb. c.lås'),

  ('parkeringssensor (bag)','parkeringssensor (bag)'),

  ('parkeringssensor (for)','parkeringssensor (for)'),

  ('ratgearskifte','ratgearskifte'),

  ('fartpilot','fartpilot'),

  ('kørecomputer','kørecomputer'),

  ('infocenter','infocenter'),

  ('startspærre','startspærre'),

  ('varme i forrude','varme i forrude'),

  ('auto. nedbl. Bakspejl','auto. nedbl. Bakspejl'),

  ('udv. temp. måler','auto. nedbl. Bakspejl'),

  ('regnsensor','regnsensor'),

  ('sædevarme','sædevarme'),

  ('højdejust. forsæder','højdejust. forsæder'),

  ('højdejust. førersæde','højdejust. førersæde'),

  ('el indst. forsæder','el indst. forsæder'),

  ('el indst. førersæde','el indst. førersæde'),

  ('el indst. førersæde m. memory','el indst. førersæde m. memory'),

  ('soltag','soltag'),

  ('el-soltag','el-soltag'),

  ('glastag','glastag'),

  ('el-ruder','el-ruder'),

  ('4x el-ruder','4x el-ruder'),

  ('el-spejle','el-spejle'),

  ('el-klapbare sidespejle','el-klapbare sidespejle'),

  ('el-klapbare sidespejle m. varme','el-klapbare sidespejle m. varme'),

  ('el-spejle m/varme','el-spejle m/varme'),

  ('nøglefri betjening','nøglefri betjening'),

  ('automatisk parkerings system','automatisk parkerings system'),

  ('360° kamera','360° kamera'),

  ('bakkamera','bakkamera'),

  ('adaptiv fartpilot','adaptiv fartpilot'),

  ('automatisk start/stop','automatisk start/stop'),

  ('el betjent bagklap','el betjent bagklap'),

  ('dæktryksmåler','dæktryksmåler'),

  ('adaptiv undervogn','adaptiv undervogn'),

  ('elektrisk parkeringsbremse','elektrisk parkeringsbremse'),

  ('træthedsregistrering','træthedsregistrering'),

  ('skiltegenkendelse','skiltegenkendelse'),

  ('CD','CD'),

  ('CD/radio','CD/radio'),

  ('radio med CD-boks','radio med CD-boks'),

  ('DAB radio','DAB radio'),

  ('DAB+ radio','DAB+ radio'),

  ('navigation','navigation'),

  ('multifunktionsrat','multifunktionsrat'),

  ('håndfrit til mobil','håndfrit til mobil'),

  ('bluetooth','bluetooth'),

  ('musikstreaming via bluetooth','musikstreaming via bluetooth'),

  ('nightvision','nightvision'),

  ('digitalt cockpit','digitalt cockpit'),

  ('headup display','headup display'),

  ('Android Auto','Android Auto'),

  ('Apple CarPlay','Apple CarPlay'),

  ('Internet','Internet'),

  ('trådløs mobilopladning','trådløs mobilopladning'),

  ('SD kortlæser','SD kortlæser'),

  ('USB tilslutning','USB tilslutning'),

  ('AUX tilslutning','AUX tilslutning'),

  ('armlæn','armlæn'),

  ('isofix','isofix'),

  ('bagagerumsdækken','bagagerumsdækken'),

  ('kopholder','kopholder'),

  ('stofindtræk','stofindtræk'),

  ('dellæder','dellæder'),

  ('læderindtræk','læderindtræk'),

  ('kunstlæder','kunstlæder'),

  ('splitbagsæde','splitbagsæde'),

  ('læderrat','læderrat'),

  ('el komfortsæder','el komfortsæder'),

  ('sportssæder','sportssæder'),

  ('integrerede børnesæder','integrerede børnesæder'),

  ('3 individuelle sæder i bag','3 individuelle sæder i bag'),

  ('lygtevasker','lygtevasker'),

  ('tågelygter','tågelygter'),

  ('bi-xenon','bi-xenon'),

  ('xenonlys','xenonlys'),

  ('automatisk lys','automatisk lys'),

  ('fjernlysassistent','fjernlysassistent'),

  ('kurvelys','kurvelys'),

  ('LED kørelys','LED kørelys'),

  ('fuld LED forlygter','fuld LED forlygter'),

  ('airbag','airbag'),

  ('db. airbags','db. airbags'),

  ('4 airbags','4 airbags'),

  ('6 airbags','6 airbags'),

  ('7 airbags','7 airbags'),

  ('8 airbags','8 airbags'),

  ('9 airbags','9 airbags'),

  ('10 airbags','10 airbags'),

  ('ABS','ABS'),

  ('antispin','antispin'),

  ('ESP','ESP'),

  ('servo','servo'),

  ('vognbaneassistent','vognbaneassistent'),

  ('blindvinkelsassistent','blindvinkelsassistent'),

  ('automatisk nødbremsesystem','automatisk nødbremsesystem'),

  ('sænket','sænket'),

  ('tagræling','tagræling'),

  ('tonede ruder','tonede ruder'),

  ('mørktonede ruder i bag','mørktonede ruder i bag'),

  ('afhentning','afhentning'),

  ('1 ejer','1 ejer'),

  ('ikke ryger','ikke ryger'),

  ('nysynet','nysynet'),

  ('lev. nysynet','lev. nysynet'),

  ('service ok','service ok'),

  ('brugtbilsattest','brugtbilsattest'),

  ('træk','træk'),

  ('aftag. træk','aftag. træk'),

  ('svingbart træk (manuel)','svingbart træk (manuel)'),

  ('svingbart træk (elektrisk)','svingbart træk (elektrisk)'),

  ('diesel partikel filter','diesel partikel filter'),

  ('tidligere undervognsbehandle','tidligere undervognsbehandle'),
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
   price= models.DecimalField(max_digits=10, decimal_places=0,verbose_name='pris')
   reduced_price= models.DecimalField(max_digits=10, decimal_places=0,null=True,blank=True,verbose_name='nedsat pris')
   description = RichTextField(verbose_name='beskrivelse')
   car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
   car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   car_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   car_photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   car_photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   car_photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   car_photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
   features = MultiSelectField(choices=features_choices,verbose_name='funktioner')
   body_style = models.ForeignKey("Style",null=True, blank=True, on_delete=models.SET_NULL,verbose_name='bil kaross stil') 
   transmission = models.CharField(choices=transmission_choices, max_length=25,verbose_name='gear')
   km = models.IntegerField()
   vehicle_number = models.CharField(null=True, blank=True, max_length=25,verbose_name='nummerplade')
   doors = models.CharField(choices=door_choices, max_length=10,verbose_name='døre')
   fuel_type = models.CharField(choices=fuel_choices, max_length=10,verbose_name='brændstoftype')
   is_featured = models.BooleanField(default=False,verbose_name='er nyhed')
   is_sold = models.BooleanField(default=False,verbose_name='Solgt')
   created_date = models.DateTimeField(default=datetime.now, blank=True)


   def __str__(self):
      return self.car_title



   def car_count(self):
     return self.objects.all().count()   

