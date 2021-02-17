from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255,verbose_name='betegnelse')
    description = RichTextField(verbose_name='beskrivelse')
    photo = models.ImageField(upload_to='photos/%Y/%M/%D')
    facebook_link = models.URLField(max_length=255)
    twitter_link = models.URLField(max_length=255)
    instagram_link = models.URLField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    is_aboutPage = models.BooleanField(default=False,verbose_name='er på (about sida)')
    

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def full_name(self):
        return self.first_name + ' ' + self.last_name

class BusinessInfo (models.Model):
  name_title = models.CharField(max_length=255,verbose_name='Navn')
  phone_number = models.CharField(max_length=255,verbose_name='Telefonnummer')
  email_address = models.CharField(max_length=255,verbose_name='Email adresse')
  opening_hours = models.CharField(max_length=255,verbose_name='Åbningstider')   

  def save(self):
      count = BusinessInfo.objects.all().count()
      # this will check if the variable exist so we can update the existing ones
      save_permission = BusinessInfo.has_add_permission(self) 
      # if there's more than two objects it will not save them in the database
      if count < 2:
          super(BusinessInfo, self).save()
      elif save_permission:
          super(BusinessInfo, self).save()

  def has_add_permission(self):
      return BusinessInfo.objects.filter(id=self.id).exists()        
