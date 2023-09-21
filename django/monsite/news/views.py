from django.shortcuts import render,redirect
#NameForm
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
import datetime as dt
from news.models import Artist
from django.http import Http404
from news.models import Article
from django.template import Context
from django import forms
import django_excel as excel
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from news.models import Person
from news.forms import UploadFileForm
#Eleve.objects.filter(nom__startswith="Ma").count()
#documents
#simple_upload
#home
#post_new
#post_new
#artiste
#date_actuelle
#addition
#view_article
#list_articles
#view_redirection
#year_archive
#index
#month_archive
#age_archive
#contact
#get_question
#home_view
#nom_artiste
# display
# voir_contacts
#import django.views.generic
#dir(django.views.generic)
#comment faire pour appeler notre template, et générer la réponse à partir de celui-ci ?
#render est la méthode de la classe django.shortcuts
#date
#noms
#artiste
#upload


##################Afficher la table
#from django.shortcuts import render_to_response


#nom_artiste

##Model Artist
#import_artist >>>>>
from news.forms import UploadFileForm
from news.forms import ArtistForm
from news.models import Artist

def import_artist(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                model=Artist,
                mapdict=['name'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request,'news/upload_form.html',{'form': form})

#import_sheet
def nom_artiste(request):
    noms = Artist.objects.all()
    context={'noms': noms}
    return render(request,'news/nom_artiste.html',context)

def post_new(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artiste = form.save(commit=False)
            artiste.name = request.POST['name']
            artiste.save()
            return redirect('news/nom_artiste.html')
    else:
        form = ArtistForm()
    return render(request,'news/post_edit.html',{'form':form})

#get_name
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArtistForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form_name = form.cleaned_data['name']
            #envoi = True
            saving_all = models.Contact.objects.create(email=form_name) 
            return HttpResponse('Success')
            # redirect to a new URL:
            #return HttpResponseRedirect('https://docs.djangoproject.com/fr/3.0/topics/forms/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArtistForm()
    return render(request, 'news/name.html', {'form': form})

def detailT(request, album_id):
    id = int(album_id) # make sure we have an integer.
    album = ALBUMS[id] # get the album with its id.
    artists = " ".join([artist['name'] for artist in album['artists']]) # grab artists name and create a string out of it.
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)

def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists = " ".join([artist.name for artist in album.artists.all()])
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
    return HttpResponse(message)

def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Aucun artiste n'est demandé"
    else:
        albums = [
            album for album in ALBUMS
            if query in " ".join(artist['name'] for artist in album['artists'])
        ]
        if len(albums) == 0:
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            albums = ["<li>{}</li>".format(album['name']) for album in albums]
            message = """
                Nous avons trouvé les albums correspondant à votre requête ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(albums))
    return HttpResponse(message)


def voir_contacts(request):
    contacts = ArtisteTable(Contact.objects.all())
    return render(request, 'news/voir_contacts.html',{'contacts':contacts})
#news:
#contact
from news.tables import *
def artiste(request):
    artistes = Artist.objects.all()
    return render(request,'news/artiste.html', {'artistes': artistes})


#from django.shortcuts import render_to_response

def home(request):
    artiste = Artist.objects.all()
    return render(request,'news/artiste.html', {'artiste': artiste})

################################################################################################################



################################################################################################################
from django.views.generic import UpdateView
from news.models import Person
from news.forms import PersonForm

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'news/person_form.html'
#person_update_form
#---------------------------------------------------------------------------------------------------------

from news.resources import PersonResource
from news.models import Person
from .forms import PersonForm
#PersonForm
#form
#nom_artiste
#edit
#import_sheet
#name_columns_by_row
##Model Person
#django_excel.ExcelMixin.save_to_database(model=None, initializer=None, mapdict=None, **keywords)
def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                model=Person,
                mapdict=['name','email','birth_date','location'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request,'news/upload_form.html',{'form': form})


def AfficherPersonne(request):
    tab = Person.objects.all()
    context={'tab': tab}
    return render(request,'news/AfficherPersonne.html',context)

def post_new_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            persone = form.save(commit=False)
            persone.name = request.POST['name']
            persone.email = request.POST['email']
            persone.birth_date = request.POST['birth_date']
            persone.location = request.POST['location']
            persone.save()
            return redirect('news/AfficherPersonne.html')
    else:
        form = PersonForm()
    return render(request,'news/edit_person.html',{'form':form})

def person_form(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            persone = form.save(commit=False)
            persone.name = request.POST['name']
            persone.email = request.POST['email']
            persone.birth_date = request.POST['birth_date']
            persone.location = request.POST['location']
            persone.save()
            return redirect('news/person_form.html')
    else:
        form = PersonForm()
    return render(request,'news/edit_person.html',{'form':form})

###############################################################################################"""


#########################################################################################



def searchT(request):
    pass


def searchT(request):
    obj = str(request.GET)
    query = request.GET['query']
    message = "propriété GET : {} et requête : {}".format(obj, query)
    return HttpResponse(message)



############################################################################################

from .models import ALBUMS

def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)

#text="<a href="{% url "afficher_article" 42 %}">Lien vers mon super article N° 42 </a>"
###########################################################################

import pytz
def date_fuseau_horraire(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'news/date_fuseau_horraire.html', {'timezones': pytz.common_timezones})


def home_view(request): 
    #print(request.POST) 
    return render(request,"news/home.html",{}) 

# Create your views here.
def redirection(request):
   #today = dt.datetime.now().date()
   #today = dt.datetime(int(2005), int(5), 1)
   today = dt.datetime.now()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return redirect("https://www.djangoproject.com")
   
def hello(request):
   today = dt.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek})

###################################################################################################	
def viewArticleY(request, articleId):
   """ A view that display an article based on his ID"""
   text = "Displaying article Number : %s" %articleId
   return redirect(viewArticles, year = "2045", month = "02")

def viewArticlesY(request, year, month):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)
   
def viewArticles(request, articleId):
   """ A view that display an article based on his ID"""
   text = "Displaying article Number : %s" %articleId
   return HttpResponse(text)
	
def viewArticlesT(request, year, month):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)
   
###########################################################################################"""""
from datetime import datetime
from django.shortcuts import render

def date_actuelle(request):
    return render(request,'news/date.html',{'date': datetime.now()})
#addition

def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request,'news/addition.html', locals())
##################################################################################################"""""""


################################################################################################"
from django.http import HttpResponse, Http404
def view_article(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if id_article > 100:
        raise Http404
    return HttpResponse('<h1>Mon article ici</h1>')

def view_article1(request, id_article):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse("Vous avez demandé l'article n° {0} !".format(id_article))

def view_article(request, id_article):
    if id_article > 100:
        raise Http404
    return redirect('view_redirection',id_article=42)

#path('article/<int:id_article>$', views.view_article, name='afficher_article'),
#return redirect('afficher_article', id_article=42)

#####################################################################################################################
	

#---------------------------------------------------------------
from django.shortcuts import redirect
def list_articles(request, year, month):
    # Il veut des articles ? Soyons fourbe et redirigeons-le vers djangoproject.com
    return redirect("https://www.djangoproject.com")

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
    return HttpResponse("Vous avez demandé les articles de {0} {1}.".format(month, year))

#########################################################################################################"
	

from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime


def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")

def accueil(request):
    date_actuelle = datetime.now()
    # […] Récupération d'autres données (exemple : une liste de news)
    return render(request,'accueil.html', locals())

def contact(request):
    return render(request,'contact.html', {'date_actuelle': datetime.now()})
	
########################################################################################################"

from django.http import HttpResponse, Http404
from django.shortcuts import redirect

from .models import Article
def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)


from django.http import HttpResponse

def date(request):
    # Some Date Object, for example a default generated by datetime
    myDate = datetime.now()
    # Render Some Template with a parameter accesible as date
    return render(request, 'news/index.html', {'myDate': myDate})


##-------------------------------------------------------------------------------
def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)

def indexT(request):
    # request albums
    albums = Album.objects.filter(available=True).order_by('-created_at')[:2]
    # then format the request.
    # note that we don't use album['name'] anymore but album.name
    # because it's now an attribute.
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    return HttpResponse(message)

def indexT(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:2]
    return HttpResponse(template.render({'albums': albums}, request=request))

def indexT(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:2]
    context = {
        'albums': albums
    }
    return HttpResponse(template.render(context, request=request))
#-----------------------------------------------------------------------------------------------


def month_archive(request, year, month=1):
    return HttpResponse('Article de %s/%s' % (year, month))
#request est une instance de HttpResponse

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'news/accueil.html', {'articles':articles})


# Il faut ajouter l'import get_object_or_404, attention !
from django.shortcuts import render, get_object_or_404

def lire(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article': article})
	
def lire(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'blog/lire.html', {'article': article})

def lire(request, id):
    """ Afficher un article complet """
    pass # Le code de cette fonction est donné un peu plus loin.

def age_archive(request, year):
    return HttpResponse('Article de %s/%s' % (year))
#request est une instance de HttpResponse

#############################################################################################
#clean_message
##Formulaire
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':# S'il s'agit d'une requête POST
        form = ContactForm(request.POST)# Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            #Ici nous pouvons traiter les données du formulaire
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']
            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
            envoi = True
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ContactForm()# Nous créons un formulaire vide
    return render(request, 'news/contact.html',locals())

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import QuestionForm
from django.shortcuts import render 
from . import forms
from . import models
from django.http import HttpResponse 
#Contact
#{% url 'news.get_question' %}
from .models import Contact

def get_question(request): 
    formset = forms.QuestionForm() 
    if request.method == 'POST': 
        formset = forms.QuestionForm(request.POST) 
        if formset.is_valid(): 
            form_email = formset.cleaned_data['your_email']
            form_question = formset.cleaned_data['your_question']
            formset.save()
            #saving_all = models.Contact.objects.create(email=form_email, name=form_question) 
            print (form_question['your_question'])
            #return HttpResponse('Success') 
    else: 
        formset = forms.QuestionForm() 
    return render(request, 'news/name.html',{'formset':formset})


#------------------------------------------------------------------------------------------------------
##Creer un formuaire à partir d'un modèle de données
from django.shortcuts import render, redirect
from .forms import ArticleForm
from news.models import Article

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_create')
    else:
        form = ArticleForm()
    return render(request,'news/article_create.html',{'form': form})
	


from django.shortcuts import render, redirect, get_object_or_404
def article_edit(request, pk=None):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_create')
    else:
        form = ArticleForm(instance=article)

    return render(request,'news/article_edit.html',{'form': form,'article': article})


from .forms import ArticleForm, ArticleDeleteForm
def article_delete(request, pk=None):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleDeleteForm(request.POST,instance=article)
        if form.is_valid():
            article.delete()
            return redirect('article_create')
    else:
        form = ArticleDeleteForm(instance=article)
    return render(request, 'news/article_delete.html',{'form': form,'article': article,})


##-------------------Contact-----------------------------------------
def nouveau_contact(request):
    sauvegarde = False
    if request.method == "POST":
        form = NouveauContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = Contact()
            contact.nom = form.cleaned_data["nom"]
            contact.adresse = form.cleaned_data["adresse"]
            contact.photo = form.cleaned_data["photo"]
            contact.save()
            sauvegarde = True
    else:
        form = NouveauContactForm()
    return render(request,'news/contact.html', locals())
#python manage.py shell
# from news.models import Contact
# from django.core.files import File
# c = Contact(nom="Jean Dupont", adresse="Rue Neuve 34, Paris")
# photo = File(open('C:/Users/alpha/Desktop/OneDrive/PROJET_DJANGO/ProjetDjango/monsite/news/media/dupont.jpg', 'r'))
# c.photo = photo
# c.save()

#---------------------------------------------------------------------------------------

##
##
##
##
##-----------------------------------------------------------------------------------------
############################################################################################
#Importer des données de Excel vers models django
#Exporting to CSV view:

# Create your views here.
def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",file_name="download")
    else:
        form = UploadFileForm()
    return render(
        request,'news/upload_form.html',{
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })

def download(request, file_type):
    sheet = excel.pe.Sheet(data)
    return excel.make_response(sheet, file_type)


#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------






#-------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

from django.http import HttpResponse
from .resources import PersonResource


def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response


##Exporting to JSON view:
from django.http import HttpResponse
from .resources import PersonResource

def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="persons.json"'
    return response

##Exporting to Excel view:
from django.http import HttpResponse
from .resources import PersonResource

def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

#Importing Data
#Consider the file new_persons.csv
# <form method="post" enctype="multipart/form-data">
    # {% csrf_token %}
    # <input type="file" name="myfile">
    # <button type="submit">Upload</button>
# </form>

from news.resources import PersonResource
from tablib import Dataset
#simple_upload
#import_data(dataset, dry_run=False, raise_errors=False)
#https://django-import-export.readthedocs.io/en/latest/import_workflow.html
#from openpyxl.reader.excel import load_workbook
#??dataset.load
def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        imported_data = dataset.load(new_persons.read(),format='xlsx')
        result = person_resource.import_data(dataset, dry_run=False,raise_errors=False)# Test the data import
        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)# Actually import now
    return render(request,'news/import.html')


##{{form.docfile}}
##----------------------------------------------------------------------------------------

# import tablib
# tablib.import_set(your_data_stream, format='csv', headers=False)

# imported_data = Dataset().load(new_stock.read().decode(), format='csv', headers=False)
# print(imported_data)

from tablib import Dataset
def simple_upload_(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        imported_data = dataset.load(new_persons.read(),format='xlsx', headers=True)
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'news/simple_upload.html')

# import tabulate
# list(tabulate._table_formats)

######################################################################################################
##---------------------------------------------------------------------------------
#############
#model_form_upload
#simple_upload
#home

#from django.shortcuts import render, redirect
from news.models import Document
from news.forms import DocumentForm
def maison(request):
    documents = Document.objects.all()
    return render(request, 'news/maison.html',{'documents': documents })

def home(request):
    documents = Document.objects.all()
    context={'documents': documents}
    return render(request, 'news/home.html',context)

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
##################################################################
#
#

#html = t.render(Context({'name': name}))

def simple_upload__(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        context = {'uploaded_file_url': uploaded_file_url}
        return render(request, 'news/simple_upload.html',context)
    return render(request,'news/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'news/model_form_upload.html', {'form': form})


#--------------------------------------

    def clean_message(self):
        message = self.cleaned_data['message']
        if "pizza" in message:
            raise forms.ValidationError("On ne veut pas entendre parler de pizza !")
        return message # Ne pas oublier de renvoyer le contenu du champ traité

    def cleanT(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')
        if sujet and message:# Est-ce que sujet et message sont valides ?
            if "pizza" in sujet and "pizza" in message:
                raise forms.ValidationError("Vous parlez de pizzas dans le sujet ET le message ? Non mais ho !")
        return cleaned_data# N'oublions pas de renvoyer les données si tout est OK


    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message:  # Est-ce que sujet et message sont valides ?
            if "pizza" in sujet and "pizza" in message:
                msg = "Vous parlez déjà de pizzas dans le sujet, n'en parlez plus dans le message !"
                self.add_error("message", msg)
        return cleaned_data
# def model_form_upload(request):
    # if request.method == 'POST':
        # form = DocumentForm(request.POST, request.FILES)
        # if form.is_valid():
            # document = form.save(commit=False)
            # document.name = 'some_new_name'
            # document.save()
            # return redirect('model_form_upload')
    # else:
        # form = DocumentForm()
# return render(request, 'model_form_upload.html', {'form': form})


##----------------------------------------------------------------------------------