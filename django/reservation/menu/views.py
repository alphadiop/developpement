from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
# Create your views here.

def indexes(request):
    clients = Booking.objects.all()
    clients_names_and_email = [client.user_name + " - " + client.user_email for client in clients]
    clients_names_and_email_str = ",".join(clients_names_and_email)
    return HttpResponse("les clients : {0}".format(clients_names_and_email_str))


def index(request):
    clients = Booking.objects.all()
    return render(request,"menu/index.html",{"clients":clients})