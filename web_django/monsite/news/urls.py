from django.urls import path
from .import views
from django.conf.urls import url
from news import views as views
from django.urls import include, path
from news.views import *
app_name = 'news'

#upper
#{{ b.name|truncatewords:80 }}
##Model Artist
#import_artist
#news_extras.py
#post_new
#artiste
#nom_artiste
#import_sheet
#http://127.0.0.1:8000/news/noms
#http://127.0.0.1:8000/news/import
#http://127.0.0.1:8000/news/artiste
#http://127.0.0.1:8000/news/edit
#http://127.0.0.1:8000/news/search
#ça marche
#get_name
urlpatterns = [
    url(r'^noms/',views.nom_artiste,name='noms'),
    url(r'^artiste/$',views.artiste,name='artiste'),
    url(r'^import/$',views.import_artist,name='import'),
    url(r'^edit/',views.post_new,name='edit'),
]
#################################################################################################
##Model Person
#import_sheet
#ca marche
#person_form
##http://127.0.0.1:8000/news/fperson
#http://127.0.0.1:8000/news/person
##http://127.0.0.1:8000/news/pimport
##http://127.0.0.1:8000/news/accueil
##http://127.0.0.1:8000/news/aperson

#ça marche
# urlpatterns = [
    # url(r'^fperson/',views.person_form,name='fperson'),
    # url(r'^person/',views.post_new_person,name='person'),
    # url(r'^pimport/',views.import_sheet,name='pimport'),
    # url(r'^aperson/',views.AfficherPersonne,name='aperson'),
    # #url(r'^afile/',views.upload,name='afile'),
# ]
#post_new_person
#person_form
#import_sheet
#AfficherPersonne
#upload
#get_name
#################################################################################################


#################################################################################################

##http://127.0.0.1:8000/news/hello
##http://127.0.0.1:8000/news/contact
#http://127.0.0.1:8000/news/addition/1/1
##http://127.0.0.1:8000/news/noms
##http://127.0.0.1:8000/news/accueil
##http://127.0.0.1:8000/news/article/42
##http://127.0.0.1:8000/news/homes
##http://127.0.0.1:8000/news/index
##http://127.0.0.1:8000/news/date/
##http://127.0.0.1:8000/news/listes/
##http://127.0.0.1:8000/news/search/
#http://127.0.0.1:8000/news/search
#http://127.0.0.1:8000/news/listes/
#http://127.0.0.1:8000/news/1/
#http://127.0.0.1:8000/news/2/
#http://127.0.0.1:8000/news/date_actuelle
#http://127.0.0.1:8000/news/listing
#http://127.0.0.1:8000/news/accueil
#http://127.0.0.1:8000/news/hello
#http://127.0.0.1:8000/news/articles/2000/1
#http://127.0.0.1:8000/news/redirection

#http://127.0.0.1:8000/news/contact
#http://127.0.0.1:8000/news/date
#http://127.0.0.1:8000/news/home
#http://127.0.0.1:8000/news/search
#http://127.0.0.1:8000/news/display
#http://127.0.0.1:8000/news/question
#http://127.0.0.1:8000/news/artiste

#from news.views import contact ##Important car ça fonctionne : url(r'^contact/$', contact, name='contact'),
# urlpatterns = [
    # # url(r'^date/',views.date_actuelle),
    # # url(r'^home/',views.home_view,name='home'),
    # # url(r'^question/',views.get_question,name='question'),
    # # url(r'^contact/', contact, name='contact'),
    # # url(r'^person/', views.simple_upload,name='person'),
    # # url(r'^search/$',views.search,name='search'),
    # # #url(r'^contact/$',views.contact,'contact'),
    # # #url(r'^display/',views.simple_upload,'simple_upload'),

# ]
#http://127.0.0.1:8000/news/noms
#http://127.0.0.1:8000/news/edit/
#http://127.0.0.1:8000/news/import/
#http://127.0.0.1:8000/news/post_new_person

#http://127.0.0.1:8000/news/person/
#http://127.0.0.1:8000/news/aperson
#http://127.0.0.1:8000/news/afile

#http://127.0.0.1:8000/admin/news/person/import/
#upload

#simple_upload
#http://127.0.0.1:8000/news/person
#from django.conf.urls.static import static
# urlpatterns = [
    # url(r'^$', views.home, name='home'),
    # url(r'^simple/$', views.simple_upload, name='simple_upload'),
    # url(r'^form/$', views.model_form_upload, name='model_form_upload'),
# ]
#http://127.0.0.1:8000/news
#http://127.0.0.1:8000/news/simple
#http://127.0.0.1:8000/news/form
#from news.views import article_create, article_edit,article_delete

# urlpatterns = [
    # path('create/',article_create, name='article_create'),
    # path('edit/<int:pk>/',article_edit,name='article_edit'),
    # path('delete/<int:pk>/',article_delete,name='article_delete'),
# ]
#http://127.0.0.1:8000/news/create
#http://127.0.0.1:8000/news/edit/2/
#http://127.0.0.1:8000/news/delete/2/

#home_view

# urlpatterns = [
    # path('index',views.index,name='index'),
    # path('accueil',views.home,name='home'),
    # path('homes',views.home_view,name='home'),
    # path('redirection',views.redirection,name='hello'),
    # path('listing',views.listing,name='listing'),
    # path('hello',views.listing,name='hello'),
    # path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
# ]

#path('articles/<id_article>',views.view_article), 
#path('articles/<id_article>',views.view_redirection),
#path('articles/<id_article>',views.viewArticles),
#path('articles/<str:tag>', views.list_articles_by_tag),
#path('articles/<int:year>/<int:month>', views.list_articles),
#path('articles/<int:year>/',views.year_archive),
#path('articles/<int:year>/<int:month>/', views.month_archive),
#path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),


#http://127.0.0.1:8000/news/search/?query=Lulu
#http://127.0.0.1:8000/news/search/?query=Ghost
#http://127.0.0.1:8000/news/search/?query=Rosana
#http://127.0.0.1:8000/news/search/

#https://openclassrooms.com/fr/courses/4425076-decouvrez-le-framework-django/4631346-ajoutez-des-relations-entre-les-modeles
#https://docs.djangoproject.com/fr/1.11/intro/tutorial03/#writing-more-views
##expressions régulières
#^ : le schéma commence par le symbole qui suit. Chez nous il s'agit d'un groupe.
#() : les parenthèses capturent un ensemble d'une expression régulière pour en faire un groupe distinct. Cela permet de le récupérer et de le manipuler sans se soucier du reste de l'expression.
#?P<album_id> : ici nous définissons le paramètre que nous souhaitons passer à la vue : album_id.
#[0-9]+ : nous spécifions que nous attendons un ou plusieurs chiffres entre 0 et 9.
#/$ : le motif termine par une barre oblique.



#path('article/<int:id_article>$', views.view_article, name='afficher_article'),
#return redirect('afficher_article', id_article=42)

#view_redirection


#http://127.0.0.1:8000/admin/news/
#http://127.0.0.1:8000/news/42/

#accueil


#http://127.0.0.1:8000/news/addition/1/2/
#http://127.0.0.1:8000/news/addition/5/3
#http://127.0.0.1:8000/news/articles/42/

#Il existe des réponses plus spéciales permettant d’envoyer au navigateur du client 
#les codes d’erreur 404 (page non trouvée) et 
#403 (accès refusé), 
#ou encore d’effectuer des redirections.

#news.views.home ===>/news/accueil
#/news/articles/42
#/news/articles/2020/5
#/news/articles/2020/1


#urlpatterns = [
    #url('listes/',views.listing),
    #url('hello/',views.hello),
    #url('home/', news_views.home, name='home'),
#]

#urlpatterns = [
    #path('index',views.index,name='index'),
    # url(r'^article/(?P<id>\d+)$',views.view_article,name='view_article'),
    # url(r'^addition/<int:nombre1>/<int:nombre2>/', views.addition),
    # url(r'^homless',views.home,name='home'),
    # url(r'^home',views.home_view,name='home'),
    # url(r'^noms', views.nom_artiste),
    # url(r'^search/$',views.search),

    # url(r'^listes/',views.listing),
    # url(r'^(?P<album_id>[0-9]+)/$',views.detail),
#]

# urlpatterns = [
    # #url(r'^contact/$',views.contact, 'contact'),
    # #url(r'^index/',views.index,name='index'),
    # #url(r'^index/',views.index,name='index'),
    # #url(r'^index/',views.index,name='index'),
# ]
