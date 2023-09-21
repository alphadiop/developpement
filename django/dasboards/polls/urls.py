#C:\Users\alpha\OneDrive\PROJET_DJANGO\dasboards\polls\urls.py
#polls/urls.py
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    #path('home/',views.index, name='index'),
    path('',views.index, name='index'),
	path('<int:question_id>/', views.detail, name='detail'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
    path('form/', views.upload_file, name='form'),
    #path('simple/', views.simple_upload, name='form'),
]

