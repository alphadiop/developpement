from django import forms
from .models import Upload
from django.forms import ModelForm


class UploadFileForm_(forms.ModelForm):
    csv_file = forms.FileField()
    #title = forms.CharField(max_length=50)
    #file = forms.FileField()

#ou
#la class Meta permet de dire à Django quel modèle il doit utiliser 
#pour créer ce formulaire (model = Upload).
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'
        #fields = ('Segment','Country')