from django.contrib import admin

# Register your models here.

from .models import Weather,Location, Temperature

admin.site.register(Weather)
admin.site.register(Location)
admin.site.register(Temperature)