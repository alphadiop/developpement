from django import forms
# A form to upload files
class CsvImportForm(forms.Form):
    csv_file = forms.FileField()