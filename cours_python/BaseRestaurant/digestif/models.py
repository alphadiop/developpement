from django.db import models


class Rhum(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origine_vin = models.CharField(max_length=200,blank=True)



class Armagnac(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origine_vin = models.CharField( max_length=200,blank=True)



class Calvados(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origine_vin = models.CharField(max_length=200, blank=True)

class Cognac(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origine_vin = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nom
