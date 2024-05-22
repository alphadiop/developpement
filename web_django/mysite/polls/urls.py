#dans le fichier polls/urls_taxi.py
from django.urls import path
from . import views
from polls.views import home_view, export_data, import_data
from django.contrib import admin
app_name = 'polls'

#http://localhost:8000/polls/34
#http://localhost:8000/polls/34/results/
#http://localhost:8000/polls/34/vote/
#http://127.0.0.1:8000/polls/home/
##https://docs.djangoproject.com/fr/3.0/intro/tutorial01/
##https://docs.djangoproject.com/fr/3.0/intro/tutorial02/
##https://docs.djangoproject.com/fr/3.0/intro/tutorial03/
##https://docs.djangoproject.com/fr/3.0/intro/tutorial04/ ici

##https://docs.djangoproject.com/fr/3.0/intro/tutorial05/
##https://docs.djangoproject.com/fr/3.0/intro/tutorial06/
##https://docs.djangoproject.com/fr/3.0/intro/tutorial07/

##path(route, view, kwargs=None, name=None)

#http://localhost:8000/polls/34
#http://localhost:8000/polls/34/results/
#http://localhost:8000/polls/34/vote/
#http://127.0.0.1:8000/polls/5/results/
#http://127.0.0.1:8000/polls/5/detail/


#http://127.0.0.1:8000/admin/

#http://127.0.0.1:8000/polls/34/
#http://127.0.0.1:8000/polls/1/


# urlpatterns = [
    # path('', home_view, name='home'),
    # path('', export_data, name='export'),
    # path('', import_data, name='import')
# ]

# urlpatterns = [
    # # ex: #http://127.0.0.1:8000/polls/
    # path('', views.index, name='index'),
	
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
	
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
	
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
	
	# path('home/', views.home_view, name='home'),
    # path('export/', views.export_data, name='export'),
    # path('import/', views.import_data, name='import'),
# ]
#marche pas
# urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:pk>/', views.detail, name='detail'),
    # path('<int:pk>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

# ]

#http://127.0.0.1:8000/admin/


#http://127.0.0.1:8000/polls
#http://127.0.0.1:8000/polls/1/
#http://127.0.0.1:8000/polls/3/results/

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


# urlpatterns = [
    # path('', views.index, name='index'),
    # path(route='', view=views.index, kwargs=None,name='index'),
    # path(route='accueil',view=views.index, name='index'),
    # path(route='<int:question_id>/', view=views.detail, name='detail'),
    # path(route='<int:question_id>/results/', view=views.results, name='results'),
    # path(route='<int:question_id>/vote/', view=views.vote, name='vote'),
# ]

#urlpatterns = [
	#path('accueil', views.home),
	#path('date', views.date_actuelle),
	#path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
	#path('list',views.list),
	#path('crepes',views.crepes),
#]




#---------------------------------------------------------
# from django.urls import path
# # from . import views

# urlpatterns = [
    # path('date', views.date_actuelle),
    # path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
# ]

#---------------------------------------------------------------

# urlpatterns = [
    # path('article/<id_article>', views.view_article),
	# path('article/<id_article>', views.view_article),
	# #path('articles/<str:tag>', views.list_articles_by_tag), 
    # path('articles/<int:year>/<int:month>', views.list_articles),
	# path('articles/<int:year>/', views.list_articles),
	# path('date', views.date_actuelle),
    # path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
# ]


# urlpatterns = [
    # path('article/<id_article>', views.view_article), 
    # #path('articles/<str:tag>', views.list_articles_by_tag), 
    # path('articles/<int:year>/<int:month>', views.list_articles),
	# path('articles/<int:year>/', views.list_articles),
	# path('date', views.date_actuelle),
    # path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
# ]