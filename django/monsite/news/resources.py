from import_export import resources
from news.models import Person
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from news.models import Person

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        fields = ('id', 'name', 'email', 'birth_date','location',)
        #export_order = ('id', 'birth_date', 'email', 'name','location',)


#@admin.register(Person)
# class PersonResource(resources.ModelResource):
    # class Meta:
        # model=Person
