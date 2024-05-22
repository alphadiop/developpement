
from datetime import datetime
from django.shortcuts import render

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())
	

def list(request):
	return render(request,'blog/list.html',locals())

def crepes(request):
	return render(request,'blog/crepes.html',locals())
		

from django.shortcuts import render
#http://127.0.0.1:8000/blog/addition/5/
# Create your views here.
from django.http import HttpResponse

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)


#------------------------------------------------------------------------------------
def view_article(request, id_article):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse("Vous avez demandé l'article n° {0} !".format(id_article))


def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
    return HttpResponse("Vous avez demandé les articles de {0} {1}.".format(month, year))
	
# views.py
def list_articles(request, year, month=1):
    return HttpResponse('Articles de %s/%s' % (year, month))
	

from django.http import HttpResponse, Http404
def view_article_(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if id_article > 100:
        raise Http404
    return HttpResponse('<h1>Mon article ici</h1>')


#rediriger vers une autre page
from django.shortcuts import redirect

def list_articles_(request, year, month):
    # Il veut des articles ? Soyons fourbe et redirigeons-le vers djangoproject.com
    return redirect("https://www.djangoproject.com")
	
	
	
from django.http import HttpResponse, Http404
from django.shortcuts import redirect

def view_article(request, id_article):
    if id_article > 100:
        raise Http404
    return redirect(view_redirection)

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")
	

#----------------------------------------------------------------------------
 # comment faire pour appeler notre templates, et générer la réponse à partir de celui-ci ?
 # La fonction render  a été conçue pour résoudre ce problème.
 
# La fonction render  est en réalité une méthode de django.shortcut  
# qui nous simplifie la vie : elle génère un objet HttpResponse après avoir traité notre templates.
# Pour les puristes qui veulent savoir comment cela fonctionne en interne, 
# n’hésitez pas à aller fouiller dans la documentation officielle.

