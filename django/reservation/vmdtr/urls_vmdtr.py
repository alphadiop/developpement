from django.urls import path
from . import views

app_name = "vmdtr"

urlpatterns = [
    path("", views.index,name='index'),
]
