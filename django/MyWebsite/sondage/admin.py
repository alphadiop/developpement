"""
http://localhost:8000/sondage/
#Username : admin
#Email address : alphadiop@gmail.com
#Password : diop
"""
#CsvImportForm
import csv
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import path
from django.contrib import admin,messages
from sondage.models import Choice
from sondage.models import Question
from sondage.models import Member
from sondage.models import Account
from django import forms
from sondage.models import Account
from django.shortcuts import render
from django.shortcuts import redirect
from sondage.forms import MemberForm,PersonForm,CsvImportForm
from django.http import HttpResponse
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from sondage.models import Person
#from django.contrib.auth.models import User, Group
#from export_csv import ExportCsvMixin
#from django.contrib.admin import AdminSite
#Register your models here.
#sondage/admin.py




#Personnalisation de la classe AdminSite
class QuestionAdmin(admin.ModelAdmin):
    model=Question
    fields = ['pub_date', 'question_text']

admin.site.register(Question,QuestionAdmin) #Faut importer le modèle avant de le rendre modifiable via l'interface admin
admin.site.register(Choice)

#https://books.agiliq.com/projects/django-admin-cookbook/en/latest/import.html
#CsvImportForm
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected"
    
@admin.register(Member)
class HeroAdmin(admin.ModelAdmin,ExportCsvMixin):#HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
    form = MemberForm
    #model=Member
    #fields = ['full_name','email','title','city',]
    #actions = ["export_as_csv"]
    #change_list_template = "admin/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('import-csv/', self.import_csv),]
        return my_urls + urls
        
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
    def save_model(self, request, obj, form, change):
        csv_file = form.cleaned_data["csv_file"]
        category, _ = Category.objects.get_or_create(name=csv_file)
        obj.category = category
        super().save_model(request, obj, form, change)
        
    def export_csv(self, request):
        person_resource = PersonResource()
        dataset = person_resource.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="persons.csv"'
        return response
        
    def export_json(self, request):
        person_resource = PersonResource()
        dataset = person_resource.export()
        response = HttpResponse(dataset.json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="persons.json"'
        return response
        
    def export_xls(self, request):
        person_resource = PersonResource()
        dataset = person_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="persons.xls"'
        return response
    
    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
 
            # Create Hero objects from passed in data
            file_data = csv_file.read().decode("utf-8")          
            lines = file_data.split("\n")
            #lines = file_data.split(";")

            #print(lines)
            #loop over the lines and save them in db. If error shows up , store as string and then display
            for line in lines:                                        
                fields = line.split(",")
                if len(fields) >= 5:
                    # Skip the list of column names i.e 'id', 'first_name' etc
                    if fields[0] != 'id':
                        # remove starting and trailing spaces from city.
                        #city = fields[4].strip()
                        # create Member object from the csv rows.
                        Member.objects.create(
                                id = fields[0], 
                                first_name = fields[1], 
                                email = fields[2], 
                                title = fields[3], 
                                city = fields[4], 
                                              )
       
            self.message_user(request, "Your csv file has been imported")
 
            return redirect("..")
            #return HttpResponseRedirect(reverse(''))
 
        form = CsvImportForm()
        #form = CsvImportForm(data_dict)
        payload = {"form": form}
        #admin_import_csv
        return render(request, "admin/csv_form.html", payload)





#Membre
#import tablib
#from import_export.fields import Field
#from import_export import resources
#from sondage.models import Book


#from sondage.admin import MemberResource
#dataset = MemberResource().export()
#print(dataset.csv)

#member_resource = resources.modelresource_factory(model=Member)()
#dataset = tablib.Dataset(['', 'New member'], headers=['id', 'full_name'])
#result = member_resource.import_data(dataset, dry_run=True)
#print(result.has_errors())



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'uuid')

admin.site.register(Account, ContactAdmin)


#admin.site.register(Member,HeroAdmin)
#admin.site.unregister(User)
#admin.site.unregister(Group)
#HeroAdmin

#Personnalisation


#@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    model=Person
    fields =["name","email","birth_date","location",]
    #pass
admin.site.register(Person,PersonAdmin)
#Remarque : ImportExportModelAdmin doit être antérieur 
#à admin. ModelAdmin dans la séquence d’héritage multiple pour éviter l’erreur MRO (Method Resolution Order).

# Étape 1: Installez django-import-export via pip
# Étape 2 : Ajouter import_export à INSTALLED_APPS dans settings.py
# Étape 3 : Importer et hériter de ImportExportModelAdmin dans admin.py
# Étape 4 : Définir import_export autorisations d’application sous settings.py (si nécessaire)