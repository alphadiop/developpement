from django.urls import path
from . import views
app_name = 'vin'
urlpatterns = [
    path('', views.index,name="index"),
]
