from django.contrib import admin

from .models import *

class GardenAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')

admin.site.register(Garden, GardenAdmin)

class DataAdmin(admin.ModelAdmin):
    list_display = ('garden', 'temperature', 'humidity')
    list_filter = ('garden',)

admin.site.register(Data, DataAdmin)
