from django.shortcuts import render

# Create your views here.
#webapp/views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>HEY!</h2>")