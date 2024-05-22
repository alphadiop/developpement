"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# L’étape suivante est de faire pointer la configuration d'URL racine 
# vers le module polls.urls. Dans mysite/urls_taxi.py, ajoutez une importation django.urls.include
# et insérez un appel include() dans la liste urlpatterns, ce qui donnera
#diop
#Ibrahima1
from django.contrib import admin
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls',namespace="polls")),
    path('admin/', admin.site.urls),
]

#
#http://localhost:8000/accueil
#http://localhost:8000/date
#http://127.0.0.1:8000/addition/5/3
#http://localhost:8000/list
#http://localhost:8000/crepes

