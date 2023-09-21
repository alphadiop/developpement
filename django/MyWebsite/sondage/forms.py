#En HTML, un formulaire est un ensemble d’éléments à l’intérieur des balises <form>...</form> 
#qui permettent à un visiteur d’effectuer des actions comme 
    #saisir du texte, 
    #sélectionner des options, 
    #manipuler des objets 
    #ou des contrôles, et ainsi de suite, puis d’envoyer ces informations au serveur.
    
#En plus de ses éléments <input>, un formulaire doit préciser deux choses :

#où : l’URL vers laquelle les données correspondant à la saisie de l’utilisateur doivent être renvoyées
#comment : la méthode HTTP utilisée pour renvoyer les données

#vous pourriez avoir un modèle BlogComment et vouloir 
#créer un formulaire permettant d’envoyer des commentaires. 
#Dans ce cas, il serait redondant de devoir définir les types de champs du formulaire, 
#car vous avez déjà défini des champs au niveau du modèle.

#C’est pour cette raison que Django fournit une classe utilitaire 
#permettant de créer une classe de formulaire Form à partir d’un modèle Django.

#/.../crmeasy/crmapp/accounts

from django import forms
from sondage.models import Question
#from django.forms import ModelForm
from sondage.models import Member
from sondage.models import Account
from sondage.models import Person

#--------------------------------------------------------
#ce formulaire est basique ! pas de modèle correspondant
class ContactForm(forms.Form):
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print (self.cleaned_data)

        
class QuestionForm(forms.Form):
    title = forms.CharField(label='Questions')
    pub_date = forms.DateField()
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()
   
#formulaire simple : forms.Form
#formulaire à partir d'un modèle de données : forms.ModelForm
#----------------------------------------------------


class PersonForm(forms.ModelForm):
    #csv_file = forms.FileField()
    class Meta:
        model = Person
        fields = ("id","name","email","birth_date","location",)
        #fields = '__all__'


class QuestionFormu(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        
        

    #attacher le formulaire à un modèle qui existe
    #ou formulaire de connexion
class MemberForm(forms.ModelForm):
    category_name = forms.CharField()

    class Meta:
        model = Member
        fields = ("id","full_name", "email", "title","city",)
        
        widgets = {
            'id': forms.TextInput(
                attrs={
                    'placeholder': 'Prénom et Nom',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
                        'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Prénom et Nom',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Adresse Email',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Titre',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'bio': forms.Textarea(
                attrs={
                    'placeholder': 'Bio',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                    'rows': 4,
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'Ville',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            )
        }
 #classe MemberForm qui hérite de django.forms.ModelForm et dans la classe Meta, 
 #nous spécifions que le modèle rattacher à ce formulaire est la classe "Member"
 

#https://www.ultimatedjango.com/learn-django/lessons/newedit-contact-enable-ajax-2/side/
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'desc', 'address_one',
                  'address_two', 'city', 'state', 'phone',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder':'Company',
                    'class':'col-md-12 form-control'
                }
            ),
            'desc': forms.Textarea(
                attrs={
                    'placeholder':'Enter a description',
                    'class':'form-control'
                }
            ),
            'address_one': forms.TextInput(
                attrs={
                    'placeholder':'Street Address',
                    'class':'gi-form-addr form-control'
                }
            ),
            'address_two': forms.TextInput(
                attrs={
                    'placeholder':'Suite, PO, etc',
                    'class':'gi-form-addr form-control'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder':'City',
                    'class':'gi-form-addr form-control'
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'placeholder':'State',
                    'class':'gi-form-addr form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder':'Phone',
                    'class':'gi-form-addr form-control'
                }
            ),
        }