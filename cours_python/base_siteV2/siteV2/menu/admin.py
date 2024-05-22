from django.contrib import admin
from .models import Nouvelle_objet, Categorie


class Nouvelle_objetAdmin(admin.ModelAdmin):
    list_display = ("nom_objet","prix","origine","commentaire")
    search_fields = ["nom_objet"]

admin.site.register(Nouvelle_objet,Nouvelle_objetAdmin)
admin.site.register(Categorie)
