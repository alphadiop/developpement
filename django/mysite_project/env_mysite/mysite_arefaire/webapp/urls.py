from django.conf.urls import url
from . import views

#webapp/urls.py
urlpatterns = [
    url(r'^$', views.index, name='index'),
]