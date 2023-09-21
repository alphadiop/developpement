"""reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path,include

# urls du projet va appeler urls de l'application
# remarquer que chaque application est prefixé par son nom
# mais ça pouvait être n'importe quel nom
urlpatterns = [
    path("", include("main.urls")),
    path("admin/", admin.site.urls),
    path("booking/", include("booking.urls")),
    path("menu/", include("menu.urls")),
    path("api/", include("booking.api_urls")),
]
