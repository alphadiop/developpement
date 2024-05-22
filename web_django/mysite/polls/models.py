# Create your models here.
#polls/models.py¶
from django.db import models

import datetime
from django.utils import timezone
#https://docs.djangoproject.com/fr/3.0/ref/models/

#python manage.py sqlmigrate polls 0001


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
		
    def __str__(self):
        return self.question_text
		
    # def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
	
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(blank=True)
    day_started = models.DateField()
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.first_name
#python -m pip install -r requirements.txt
#pip install django-import_export
#Pour toute modification du model
# python manage.py makemigrations polls
# python manage.py migrate
# python manage.py runserver

#https://docs.djangoproject.com/fr/1.11/ref/contrib/gis/tutorial/
# import pandas as pd	
# import csv
# class Donnes(models.Model):
	# df = pd.read_csv("C:\Users\alpha\Desktop\OneDrive\PROJET_PYTHON\Ecommerce Pucharse\ecommerce.txt")
	# # Make a row iterator (this will go row by row)
	# iter_data = df.iterrows()
	# map(lambda(i,data) : Product.objects.create(**dict(data)),iter_data

# class all_products(models.Model):
    # def get_all_products():
        # items = []
        # with open("C:\Users\alpha\Desktop\OneDrive\PROJET_PYTHON\Ecommerce Pucharse\ecommerce.txt","r") as fp:
            # # You can also put the relative path of csv file
            # # with respect to the manage.py file
            # reader1 = csv.reader(fp, delimiter=';')
            # for value in reader1:
                # items.append(value)
        # return items


# import pandas as pd
# class produits(models.Model):
	# def get_produits():
		# df = pd.read_csv('C:\Users\alpha\Desktop\OneDrive\PROJET_PYTHON\Ecommerce Pucharse\ecommerce.txt', sep=';')
		# products = []
		# for i in range(len(df)):
			# products.append(Product(
			# name=df.iloc[i][0]
			# description=df.iloc[i][1]
			# price=df.iloc[i][2]
			# )
		# )
	# return Product.objects.bulk_create(products)
#1. python manage.py makemigrations polls
#2. python manage.py migrate
#3. python manage.py sqlmigrate polls 0001


#from polls.models import Choice, Question
#from django.utils import timezone
# python manage.py makemigration
# 
# python manage.py createsuperuser
# python manage.py loaddata category.json book.json
# python manage.py runserver


		


# import datetime

# from django.db import models
# from django.utils import timezone

# class Question(models.Model):
    # # ...
    # def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)