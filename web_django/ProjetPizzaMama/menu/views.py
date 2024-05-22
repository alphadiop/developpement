from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza
from django.core import serializers

# Create your views here.

def index(request):
    """
    pizzas = Pizza.objects.all()
    pizza_names = [pizza.nom + " :" + str(pizza.prix)+" €" for pizza in pizzas]
    pizzas_names_str = ",".join(pizza_names)
    return HttpResponse(pizzas_names_str)
    """
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request,template_name='menu/index.html',context={'pizzas':pizzas})


def api_get_pizzas(request):
    pizzas = Pizza.objects.all().order_by('prix')
    json = serializers.serialize(format="json",queryset=pizzas)
    return HttpResponse(json)