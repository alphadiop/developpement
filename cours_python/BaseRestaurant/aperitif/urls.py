from django.urls import path
from . import views



app_name = 'aperitif'
urlpatterns = [
    path('', views.index,name="index"),
]