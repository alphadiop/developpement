from django.urls import path
from . import views
app_name = 'alcool'
urlpatterns = [
    path('', views.alcool, name="index"),

        ]