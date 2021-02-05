from django.contrib import admin
from .models import Team, BusinessInfo
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="35" style="border-radius: 50%" />'.format(object.photo.url))

    thumbnail.short_description = 'photo'

    list_display = ['full_name', 'thumbnail', 'designation', 'created_date']
    list_display_links = ('full_name', 'thumbnail')

    class Meta:
        model = Team

class BusinessInfoAdmin(admin.ModelAdmin):
  
  list_display = ['name_title', 'phone_number', 'email_address', 'opening_hours']



admin.site.register(Team, TeamAdmin)
admin.site.register(BusinessInfo, BusinessInfoAdmin)
