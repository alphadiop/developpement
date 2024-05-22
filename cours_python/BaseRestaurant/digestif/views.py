from django.shortcuts import render

from .models import Rhum,Armagnac,Calvados,Cognac
def index(request):
    Rhums=Rhum.objects.all()
    Armagnacs=Armagnac.objects.all()
    Calvadoss=Calvados.objects.all()
    Cognacs = Cognac.objects.all()

    return render(request, 'digestif/index.html', {'Rhums': Rhums, 'Armagnacs': Armagnacs,
                                                   'Calvadoss': Calvadoss,'Cognacs': Cognacs})
