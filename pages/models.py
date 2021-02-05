from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%M/%D')
    facebook_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    instagram_link = models.URLField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def full_name(self):
        return self.first_name + ' ' + self.last_name

class BusinessInfo (models.Model):
  name_title = models.CharField(max_length=255,verbose_name='Navn')
  phone_number = models.CharField(max_length=255,verbose_name='Telefonnummer')
  email_address = models.CharField(max_length=255,verbose_name='Email adresse')
  opening_hours = models.CharField(max_length=255,verbose_name='Åbningstider')    
