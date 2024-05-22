from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
	
# Article.objects.create(titre="Bonjour", auteur="Maxime", contenu="Salut")