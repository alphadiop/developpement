from django.shortcuts import render

from .models import VinRouge,VinBlanc,VinRosee
def index(request):
    VinRouges=VinRouge.objects.all()
    VinBlancs=VinBlanc.objects.all()
    VinRosees=VinRosee.objects.all()

    return render(request, 'vin/index.html', {'VinRouges': VinRouges, 'VinBlancs': VinBlancs,
                                                   'VinRosees': VinRosees})

