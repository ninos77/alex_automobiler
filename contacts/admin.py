from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
  list_display = ('id','full_name','email','car_title','create_date')
  list_display_links = ('id','full_name')
  search_fields = ('full_name','car_title','email')
  list_per_page = 25


admin.site.register(Contact,ContactAdmin)
