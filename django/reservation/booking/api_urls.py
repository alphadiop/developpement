from django.urls import path
from . import views
# attention : un bout se trouve dans urls du projet (/api)
# ensuite l'autre partie ici (GetClients)
# du coup pour acceder au json des données : http://127.0.0.1:8000/api/GetClients
urlpatterns = [
    path("GetClients", views.api_get_clients),
]