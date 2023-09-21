#title
#Chaque modèle est une classe Python qui hérite de django.db.models.Model.
#Chaque attribut du modèle représente un champ de base de données.
#Chaque champ de votre modèle doit être une instance de la classe Field appropriée : 
#Django vous offre une API d’accès à la base de données générée automatiquement

#Chaque champ est défini comme un attribut de classe, et chaque attribut correspond à une colonne de base de données.
#voir Création de requêtes.
#Django utilise du code SQL adapté au moteur de base de données indiqué dans votre fichier de réglages.

#Les métadonnées de modèles sont « tout ce qui n’est pas un champ », 
#comme les options de tri (ordering), le nom de la table de base de données (db_table) 
#ou des noms verbeux singulier et pluriel (verbose_name et verbose_name_plural). 
#Aucune n’est obligatoire et la présence de class Meta dans un modèle est entièrement facultative

#Alors que les méthodes de Manager sont prévues pour agir au niveau des tables, 
#les méthodes de modèles agissent plutôt sur une instance particulière d’un modèle.

#template : Un bout de texte servant de base de formatage pour représenter des données. 
#Un template aide à faire la séparation claire entre des données et leur présentation.

from django.db import models
import datetime
from datetime import date
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #null=True, blank=True
    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
   

class Member(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
   
    def __str__(self):
        return self.full_name
        

#python manage.py shell
#from sondage.models import Member
#b = Member(full_name='Beatles', email='al@gmail.comme',title='Titre',city='Guyancourt')
#c = Member(full_name='Beatles', email='alp@gmail.comme',title='Titre',city='Guyancourt')
#b.save()


#python manage.py makemigrations
#python manage.py migrate

#Le nom de la table vient du nom de l'application et de celui de la classe du modèle

#from sondage.models import Choice, Question
#q = Question(question_text="What's new?", pub_date=timezone.now())
#q.save()
#q.id

#q.question_text = "What's up?"
#q.save()

#q = Question.objects.get(pk=2)
#q.choice_set.create(choice_text='Guinée', votes=0)
#q.choice_set.create(choice_text='France', votes=0)
#q.choice_set.create(choice_text='Suede', votes=0)

#q = Question.objects.get(pk=2)
#q.choice_set.create(choice_text='Guinée', votes=0)
#q.choice_set.create(choice_text='France', votes=0)
#q.choice_set.create(choice_text='Suede', votes=0)

#-----------------------------------------------------------------------------------------------------
#python manage.py makemigrations sondage
from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField
#https://www.ultimatedjango.com/learn-django/lessons/account-app-setup-create-app/side/
#b = Account(full_name='Beatles', email='al@gmail.comme',title='Titre',city='Guyancourt')
class Account(models.Model):
    uuid = ShortUUIDField(unique=True)
    name = models.CharField(max_length=80)
    desc = models.TextField(blank=True)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    phone = models.CharField(max_length=20)
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING,)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'accounts'

    def __unicode__(self):
        return u"%s" % self.name

    #@models.permalink
    def get_absolute_url(self):
        return 'account_detail', [self.uuid]

    #@models.permalink
    def get_update_url(self):
        return 'account_update', [self.uuid]

    #@models.permalink
    def get_delete_url(self):
        return 'account_delete', [self.uuid]

#https://simpleisbetterthancomplex.com/packages/2016/08/11/django-import-export.html
#https://www.programink.com/django-tutorial/django-import-export.html
#https://simpleisbetterthancomplex.com/packages/2016/08/11/django-import-export.html
#python manage.py makemigrations sondage
#python manage.py migrate

class Person(models.Model):
    name = models.CharField(max_length=30,blank=False)
    email = models.EmailField(blank=False)
    birth_date = models.DateField(default=date.today(),blank=False)#auto_now_add=True default=date.today()
    location = models.CharField(max_length=100, blank=False)
    #field = ("name","email","birth_date","location",)
    def __str__(self):
        return self.name
 #une table va être créer : "sondage_person" attention Person dévient person 