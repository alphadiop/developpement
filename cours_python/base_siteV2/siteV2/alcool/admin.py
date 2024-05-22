from django.contrib import admin
from .models import Nouvelle_objet_alcool, Categorie


class Nouvelle_objet_alcoolAdmin(admin.ModelAdmin):
    list_display = ("nom_objet","prix","origine","commentaire")
    search_fields = ["nom_objet"]

admin.site.register(Nouvelle_objet_alcool,Nouvelle_objet_alcoolAdmin)
admin.site.register(Categorie)
