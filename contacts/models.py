from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
  full_name = models.CharField(max_length=255,verbose_name='fulde navn')
  email = models.EmailField(max_length=255)
  car_id = models.IntegerField()
  car_title = models.CharField(max_length=255,verbose_name='Biltitel') 
  customer_need = models.CharField(max_length=255,verbose_name='kundebehov') 
  message = models.TextField(blank=True,verbose_name='kommentar') 
  create_date = models.DateTimeField(blank=True, default=datetime.now)

  def __str__(self):
    return self.email