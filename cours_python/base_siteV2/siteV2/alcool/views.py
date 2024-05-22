from django.shortcuts import render

from .models import Nouvelle_objet_alcool

def alcool(request):
    coktails = Nouvelle_objet_alcool.objects.filter(categorie__id__contains=4)
    spiritueux = Nouvelle_objet_alcool.objects.filter(categorie__id__contains=1)
    coktails_sans_alcools = Nouvelle_objet_alcool.objects.filter(categorie__id__contains=5)
    vins_rouges = Nouvelle_objet_alcool.objects.filter(categorie__id__contains=2)
    vins_blancs = Nouvelle_objet_alcool.objects.filter(categorie__id__contains=3)
    section = {"coktails":coktails,
               "spiritueux":spiritueux,
               "coktails_sans_alcools": coktails_sans_alcools,
               "vins_rouges": vins_rouges,
               "vins_blancs": vins_blancs,
               }

    return render(request, "alcool/index.html", section)


