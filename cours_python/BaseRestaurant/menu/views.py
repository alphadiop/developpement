from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Entree
from .models import Plat
from .models import Suggestion_Plat
from .models import Dessert
from .models import PlatMenuEnfant
from .models import PrixMenuEnfant
from .models import DessertEnfant




def index(request):
    entrees = Entree.objects.all()
    plats = Plat.objects.all()
    suggestions_plats = Suggestion_Plat.objects.all()
    desserts = Dessert.objects.all()
    plats_enfants = PlatMenuEnfant.objects.all()
    prix_enfants = PrixMenuEnfant.objects.all()
    desserts_enfants = DessertEnfant.objects.all()
    sections = (("Entrées: ", entrees), ("Plats: ", plats))


    return render(request, 'menu/index.html',{'entrees':entrees,'plats':plats,
                                              'suggestions_plats':suggestions_plats,'desserts':desserts,
                                              'plats_enfants':plats_enfants
                                              ,'prix_enfants':prix_enfants,
                                              "desserts_enfants":desserts_enfants})



def api_get_entree(request):
    entrees = Entree.objects.all()
    json = serializers.serialize("json",entrees)
    return HttpResponse(json)





