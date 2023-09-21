
# Delete your database (db.sqlite3 in my case) in your project directory
# Remove everything from __pycache__ folder under your project subdirectory
# For the application you are trying to fix, go to the folder and clear migrations and __pycache__ directories

#When you are sure you have cleared all the above files, run:

#python manage.py makemigrations
#python manage.py migrate
#ContactForm

##--------------------------------------------------
#from django.apps import apps
#news_tables = apps.get_app_config("news")
#news_tables
#news_tables.models
#-------->
#you can also get field names of particular model

#questionTable = news_tables.get_model("artist")
#questionTable._meta.get_fields()
#----->
#len(questionTable._meta.get_fields())
from django.db import models

# Create your models here.

# from django.db import models

ARTISTS = {
  'francis-cabrel': {'name': 'Francis Cabrel'},
  'lej': {'name': 'Elijay'},
  'rosana': {'name': 'Rosana'},
  'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
}

ALBUMS = [
  {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
  {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
  {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]

#################################################################################
#https://zestedesavoir.com/tutoriels/598/developpez-votre-site-web-avec-le-framework-django/263_premiers-pas/1525_la-gestion-des-fichiers/
#http://django.pyexcel.org/en/latest/
#---------------------------------------------------------------------------------------------------------
#Contact
class Artist(models.Model):
    name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name
#--------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
##pip install django-crispy-forms
from django.db import models
from django.utils import timezone
class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)
    
    def publish(self):
        self.birth_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
#python manage.py shell
# from news.models import Person
# c = Person(name="Jean Dupont", email="alpha@gjk.fr",birth_date='2019-07-13',location="Rue Neuve 34, Paris")
##Deuxième méthode pour 
from django.views.generic import CreateView
from .models import Person
class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'birth_date', 'location')
#import_sheet
#########################################################################




#CREATE TABLE news_artist("id" serial NOT NULL PRIMARY KEY, "name" varchar(200) NOT NULL UNIQUE );
class ContactT(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name
#-----------------------------------------------------------------------------------------------------

class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/")

    def __str__(self):
           return self.nom
###---------------------------------------------------------------------------------------------------------
# python manage.py makemigrations
# python manage.py migrate
#manage.py showmigrations
from django.db import models
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

#----------------------------------------------------------------------------------------------------------

####################################################################"""""
# from news.models import Contact
# from django.core.files import File
# c = Contact(nom="Jean Dupont", adresse="Rue Neuve 34, Paris")
# photo = File(open('C:/Users/alpha/Desktop/OneDrive/PROJET_DJANGO/ProjetDjango/monsite/news/media/photos.jpeg', 'r'))
# c.photo = photo
# c.save()
#----------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
class Album(models.Model):
    name = models.CharField(max_length=200,unique=True)
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    artists = models.ManyToManyField(Artist,related_name='albums',blank=True)
	
    def __str__(self):
        return self.full_name

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    album = models.OneToOneField(Album,on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE)
	
#################################################################################



from django.db import models
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)
    def __str__(self):
        return self.full_name

class Articles(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

from django.db import models
from django.utils import timezone

class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    slug = models.SlugField(max_length=100)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie',on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

# from news.models import Article
# Article.objects.create(title = 'Hello World', auteur='Alpha',slug='',contenu = 'what',date='2019-07-12',categorie = 'Python')

########################################################################################################
class Moteur(models.Model):
    nom = models.CharField(max_length=25)

    def __str__(self):
        return self.nom

class Voiture(models.Model):
    nom = models.CharField(max_length=25)
    moteur = models.OneToOneField(Moteur,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
#########################################################################################################

class Produit(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Vendeur(models.Model):
    nom = models.CharField(max_length=30)
    produits = models.ManyToManyField(Produit, through='Offre')


    def __str__(self):
        return self.nom

class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit,on_delete=models.CASCADE)
    vendeur = models.ForeignKey(Vendeur,on_delete=models.CASCADE)

    def __str__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)

##############################################################################################################


#python manage.py shell
#python manage.py shell
# from news.models import Article, Reporter

# Reporter.objects.all()
# r = Reporter(full_name='John Smith')
# r.save()
# r.full_name
# Reporter.objects.get(id=1)

# Reporter.objects.get(full_name__startswith='John')
# Reporter.objects.get(full_name__contains='mith')

# Reporter.objects.get(id=2)


# from datetime import date
# a = Article(pub_date=date.today(), headline='Django is cool',content='Yeah.', reporter=r)
# a.save()

###############################################################
# from news.models import Categorie, Article
# cat = Categorie(nom="Crêpes")
# cat.save()
# art = Article()
# art.titre = "Les nouvelles crêpes"
# art.auteur = "Maxime"
# art.contenu = "On a fait de nouvelles crêpes avec du trop bon rhum"
# art.categorie = cat
# art.save()

#article = Article(titre="Bonjour", auteur="Maxime")
#article.contenu = "Les crêpes bretonnes sont trop bonnes !"
#print (article.auteur)
#article.save()


# from importlib import reload
# reload(news.models)
# from news.models import Artist

#artiste=Artist(name="Jean")
#artiste=Artist(name="Dupont")
#artiste.save()

# <table>
# <tr>
  # <th>author</th>
  # <th>title</th>
  # <th>publication year</th>
# </tr>
# {% for b in obj %}
# <tr>
  # <td>{{ b.author }}</td>
  # <td>{{ b.title }}</td>
  # <td>{{ b.publication_year }}</td>
# </tr>
# {% endfor %}
# </table> nom_artiste

#-------------------------------------------------------------
# <form action = "" method = "POST"> 
	# {% csrf_token %} 
	# <label for="your_name">Your name: </label> 
	# <input id="your_name" type="text" name="your_name">
	# <input type="submit" value="OK"> 
# </form> 
#--------------------------------------------------------------