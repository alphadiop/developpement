from django.contrib.auth.models import User
from news.models import Person
import django_filters

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
