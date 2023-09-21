from import_export import resources
from sondage.models import Person

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person