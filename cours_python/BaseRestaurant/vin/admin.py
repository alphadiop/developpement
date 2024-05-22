from django.contrib import admin

class Vin(admin.ModelAdmin):
    list_display =('nom','prix','origine_vin')
    search_fields = ['nom']

from .models import VinRouge,VinBlanc,VinRosee
admin.site.register(VinRouge,Vin)
admin.site.register(VinBlanc,Vin)
admin.site.register(VinRosee,Vin)