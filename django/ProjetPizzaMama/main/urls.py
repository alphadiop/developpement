from django.urls import path
from . import views

app_name = "main" # nom utilisé dans le refrencement des liens
urlpatterns = [
    path('', views.index,name = 'index'),
]
