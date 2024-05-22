import django_tables2 as tables
from news.models import *
#from news.models import Artist
class ArtisteTable(tables.Table):
    class Meta:
        model = Artist