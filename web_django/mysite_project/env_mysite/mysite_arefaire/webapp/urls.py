from django.conf.urls import url
from . import views

#webapp/urls_taxi.py
urlpatterns = [
    url(r'^$', views.index, name='index'),
]