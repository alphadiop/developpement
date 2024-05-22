# users/urls.py
from django.urls import path,include
from . import views

#from django.conf.urls import url

app_name = "users"


urlpatterns = [
    path("", views.dashboard, name="dashboard"), # http://127.0.0.1:8000/users
    path("accounts/", include("django.contrib.auth.urls")), # http://127.0.0.1:8000/accounts
    path("oauth/", include(arg="social_django.urls",namespace='social')),# http://127.0.0.1:8000/oauth
    path("register/", views.register, name="register"),# http://127.0.0.1:8000/users/register
]
