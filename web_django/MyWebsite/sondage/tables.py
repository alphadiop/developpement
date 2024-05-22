from sondage.models import Member
from sondage.models import Person
from sondage.models import Question
import django_tables2 as tables

class MembreTable(tables.Table):
    class Meta:
        model = Member
        #template_name = "sondage/membre.html"
        #fields = ("full_name", )
        attrs = {'class': 'paleblue'}
      
      
class PersonTable(tables.Table):
    class Meta:
        model = Person
        #template_name = "sondage/membre.html"
        #fields = ("full_name", )
        attrs = {'class': 'paleblue'}

class QuestionTable(tables.Table):
    class Meta:
        model = Question
        #template_name = "sondage/membre.html"
        fields = ['question_text', 'pub_date']
        attrs = {'class': 'paleblue'}