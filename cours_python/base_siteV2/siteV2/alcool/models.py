from django.db import models

class Nouvelle_objet_alcool(models.Model):
        nom_objet = models.CharField(max_length=200)
        prix = models.FloatField(default=0)
        ingredient = models.CharField(max_length=200, blank=True)
        origine = models.CharField(max_length=200, blank=True)
        commentaire = models.CharField(max_length=200, blank=True)
        categorie = models.ManyToManyField("Categorie",related_name="Objet")
        def __str__(self):
                return self.nom_objet
class Categorie(models.Model):
        nom = models.CharField(max_length=100)
        def __str__(self):
                return self.nom

