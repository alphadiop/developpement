# Register your models here.
from django.contrib import admin
from import_export.fields import Field

from . import models
admin.site.register(models.Article)

##################################################################
#######------------------------------------------------

#################
#https://django-import-export.readthedocs.io/en/latest/getting_started.html
#https://github.com/django-import-export/django-import-export/tree/master/import_export
#https://django-data-importer.readthedocs.io/en/latest/readme.html
#------------------------Import-----------------

# import tablib
# from import_export import resources
# from news.models import Person
# book_resource = resources.modelresource_factory(model=Person)()
# dataset = tablib.Dataset(['','New person'], headers=['id','name','email','birth_date','location'])
# result = person_resource.import_data(dataset, dry_run=True)
# print(result.has_errors())

# result = person_resource.import_data(dataset, dry_run=False)
#-----------------------Export data-----------------------------------------
# from news.admin import PersonResource
# dataset = PersonResource().export()
# print(dataset.csv)
###################################################################

#Exemple
# python manage.py shell
# import import_export
# dir(import_export)

# from import_export import resources
# from core.models import Book

# class BookResource(resources.ModelResource):

    # class Meta:
        # model = Book