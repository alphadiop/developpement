
from django.shortcuts import render
from .models import Tapa,Champagne,Cocktail,Classique,CocktailClassique,SansAlcools,Vodka,Gin, Whiskie

def index(request):
    Tapas=Tapa.objects.all()
    Champagnes=Champagne.objects.all()
    Cocktails=Cocktail.objects.all()
    Classiques=Classique.objects.all()
    CocktailClassiques=CocktailClassique.objects.all()
    SansAlcoolss=SansAlcools.objects.all()
    Vodkas=Vodka.objects.all()
    Gins=Gin.objects.all()
    Whiskies=Whiskie.objects.all()

    return render(request, 'aperitif/index.html', {'Tapas': Tapas, 'Champagnes': Champagnes,
                                               'Cocktails': Cocktails, 'Classiques': Classiques,
                                               'CocktailClassiques': CocktailClassiques
                                                ,'SansAlcoolss': SansAlcoolss
                                                , 'Vodkas': Vodkas
                                                , 'Gins': Gins
                                                ,'Whiskies': Whiskies,})
