from django.db import (models)


class Entree(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origin_viande = models.CharField(max_length=200,blank=True)
    commentaire = models.CharField(max_length=200, blank=True)


class Plat(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origin_viande = models.CharField( max_length=200,blank=True)
    commentaire = models.CharField(max_length=200, blank=True)


class Suggestion_Plat(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origin_viande = models.CharField(max_length=200, blank=True)
    commentaire = models.CharField(max_length=200,blank=True)




class Dessert(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origin_viande = models.CharField(max_length=200, blank=True)
    commentaire = models.CharField(max_length=200, blank=True)


class PrixMenuEnfant(models.Model):
    nom_et_ou_prix = models.CharField(max_length=200, blank=True)
    prix = models.FloatField(default=0)
    origin_viande = models.CharField(max_length=200, blank=True)
    commentaire = models.CharField(max_length=200, blank=True)


class PlatMenuEnfant(models.Model):
    nom_et_ou_prix = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origin_viande = models.CharField(max_length=200, blank=True)
    commentaire = models.CharField(max_length=200, blank=True)

class DessertEnfant(models.Model):
    nom_et_ou_prix = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origin_viande = models.CharField(max_length=200, blank=True)
    commentaire = models.CharField(max_length=200, blank=True)






