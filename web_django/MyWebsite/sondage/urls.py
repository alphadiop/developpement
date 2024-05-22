# coding: utf-8
"""
http://localhost:8000/sondage/
http://localhost:8000/admin/
"""

#module sondage.urls
from django.urls import path
from django.urls import re_path
#from django.conf.urls import patterns, include, url
from sondage import views
from sondage.views import MembreListView
from sondage.views import AccountList
from sondage.views import ContactView
from sondage.models import Member
from django.views.generic import RedirectView

#le module views.py se trouve dans le dossier "sondage" d'ou from sondage import views
app_name = 'sondage'
#http://localhost:8000/admin
urlpatterns = [
    #path('',views.index,name='index'), #http://localhost:8000/sondage/
    path('', RedirectView.as_view(url='sondage/', permanent=True)),#http://localhost:8000/sondage
    path('<int:question_id>/',views.detail,name='detail'),#http://localhost:8000/sondage/1
    path('<int:question_id>/results/',views.results,name='results'),#http://localhost:8000/sondage/1/results/
    path('<int:question_id>/vote/',views.vote, name='vote'),#http://localhost:8000/sondage/1
    path('Fichier/',views.affichage_data,name='affichage_data'), #http://localhost:8000/sondage/Fichier
  
    path('Formulaire/',views.saisir_of_question,name='saisir_of_question'), #http://localhost:8000/sondage/Formulaire QuestionFormu
    path('liste-question/',views.afficher_table_question,name='afficher_table_question'), #http://localhost:8000/sondage/liste-question
    
    path('Formu/',views.home_view,name='Formu'), #http://localhost:8000/sondage/Formu 
    path('Membre/',views.homepage,name='Membre'), #http://localhost:8000/sondage/Membre
    path('tables/', views.essai_view, name='tables'),#http://localhost:8000/sondage/tables
    path('table/', views.pagination, name='table'),#http://localhost:8000/sondage/table
    path("liste/",views.AccountList.as_view(),name='account_list'),#http://localhost:8000/sondage/liste/
    #path("liste2/",views.account_detail, name='account_detail'),#http://localhost:8000/sondage/liste2/ #account_detail
    path("liste2/",views.account_cru, name='account_cru'),#http://localhost:8000/sondage/liste2/ #account_cru
    path("Imports/",views.import_csv, name='Imports'),#http://localhost:8000/sondage/Imports/ simple_upload
    path("people/", views.MembreListView.as_view(model=Member),name='membre'),#http://localhost:8000/sondage/people
    re_path(r'^contact/$', ContactView.as_view(),name='contact'),#http://localhost:8000/sondage/contact
    
    path("Import/",views.simple_upload, name='Import'),#http://localhost:8000/sondage/Import/ 
    
   
    path('Fperson', views.alimenter_form_person, name='Fperson'),#http://localhost:8000/sondage/Fperson alimenter_form_person
    path('Tperson', views.afficher_table_person, name='Tperson'),#http://localhost:8000/sondage/Tperson
    
    #path('export/csv', views.export_users_csv, name='export_users_csv'),#http://localhost:8000/sondage/export/csv
    #path('export/xls', views.export_users_xls, name='export_users_xls'),#http://localhost:8000/sondage/export/xls affi_form_person
    
]


#noter la présence "account_list" dans le templates "sondage:account_list"
#path(route, view, kwargs=None, name=None)
#path(route='', view=views.upload_csv, kwargs=None,name='upload_csv'),
#url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
#path(route='', view=views.upload_csv, kwargs=None,name='upload_csv'),uploadFile
#path(route='sondage',view=views.index),#http://localhost:8000/sondage/
#path('',views.index,name='index'), #http://localhost:8000/sondage/
