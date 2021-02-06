from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):

  def thumbnail(self, object):
      return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

  thumbnail.short_description = 'Car Image'
  list_display = ('thumbnail','car_title', 'color','make', 'model', 'year','transmission','body_style', 'fuel_type', 'is_featured','is_sold')
  list_display_links = ('thumbnail', 'car_title')
  list_editable = ('is_featured','is_sold')
  search_fields = ('description','car_title', 'make', 'model','transmission', 'year','fuel_type')
  list_filter = ('model', 'make','model', 'fuel_type')


admin.site.register(Car,CarAdmin)
