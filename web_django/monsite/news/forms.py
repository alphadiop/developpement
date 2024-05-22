from django import forms
from django.contrib import admin

#-----------------------------------------------------------------------------------------------------------------
#ArtistForm
#https://docs.djangoproject.com/fr/3.0/topics/forms/modelforms/
from django import forms
from .models import Artist
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name',]

#https://docs.djangoproject.com/fr/3.0/topics/forms/
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from news.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name','email','birth_date','location')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))
#-----------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()
#-----------------------------------------------------------------------------------------------------------------
##DocumentForm
from django import forms
from news.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description','document',)
#-----------------------------------------------------------------------------------------------------------------

#Notez forms.ModelForm et forms.Form
from django import forms
#ou
#from django.forms import ModelForm
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('titre', 'auteur','slug', 'contenu','date','categorie',)

class ArticleDeleteForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = []

# class ArticleForm(forms.ModelForm):
    # class Meta:
        # model = Article
        # exclude = ('auteur','categorie','slug')  # Exclura les champs nommés « auteur », « categorie » et « slug »


#-----------------------------------------------------------------------------------------------------------------------------


from django import forms 
class QuestionForm(forms.Form): 
    your_email = forms.EmailField() 
    your_question = forms.CharField(widget = forms.Textarea) 

from django import forms
#ContactForm
class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

#pip install django-widget-tweaks
#--------------------------------------------------------------------------------------------------------------------------
from django import forms 
from django.forms import Textarea 
from . import models 

class QuestionForm(forms.Form): 
    class Meta: 
        model = models.Contact 
        fields = ('email', 'name')
        widgets = { 
        'name': Textarea(attrs={'cols': 40, 'rows': 20}), 
     }

class UploadFileForm(forms.Form):
    file = forms.FileField()

