# Create your views here.
#personal/urls_taxi.py:
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')]
