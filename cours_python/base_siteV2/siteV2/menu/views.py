from django.shortcuts import render
from .models import Nouvelle_objet

def menu(request):
        entrees = Nouvelle_objet.objects.filter(categorie__id__contains=1)
        plats = Nouvelle_objet.objects.filter(categorie__id__contains=2)
        suggestion_plats = Nouvelle_objet.objects.filter(categorie__id__contains=6)
        desserts = Nouvelle_objet.objects.filter(categorie__id__contains=7)
        plat_enfants = Nouvelle_objet.objects.filter(categorie__id__contains=9)
        section = {
            "entrees": entrees,
            "plats": plats,
            "suggestion_plats": suggestion_plats,
            "desserts": desserts,
            "plat_enfants": plat_enfants,

            }
        return render(request,"menu/index.html",section)




