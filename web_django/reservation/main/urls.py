
from . import views
from django.urls import path,include
app_name = "main"


urlpatterns = [
    path("", views.index,name='index'),
    path("accounts/", include("django.contrib.auth.urls")), # http://127.0.0.1:8000/accounts
    path("dashboard/", views.dashboard, name="dashboard"), # http://127.0.0.1:8000/dashboard
    #path("oauth/", include(arg="social_django.urls")),# http://127.0.0.1:8000/oauth
    path("register/", views.register, name="register"),# http://127.0.0.1:8000/main/register
]
