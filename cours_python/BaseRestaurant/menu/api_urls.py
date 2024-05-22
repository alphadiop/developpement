from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [

    path('GetEntree', views.api_get_entree),
]
