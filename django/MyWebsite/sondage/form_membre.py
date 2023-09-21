from django import forms

from .models import Member

class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ("full_name", "email", "title","city",)
        
        widgets = {
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
 #nous spécifions que le modèle rattacher à ce formulaire est la classe Member