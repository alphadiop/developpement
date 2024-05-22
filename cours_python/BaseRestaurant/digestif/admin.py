from django.contrib import admin

class Digestif(admin.ModelAdmin):
    list_display =('nom','prix','origine_vin')
    search_fields = ['nom']

from .models import Rhum,Armagnac,Calvados,Cognac
admin.site.register(Rhum,Digestif)
admin.site.register(Armagnac,Digestif)
admin.site.register(Calvados,Digestif)
admin.site.register(Cognac,Digestif)