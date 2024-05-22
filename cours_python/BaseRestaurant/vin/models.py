from django.db import models


class VinRouge(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origine_vin = models.CharField(max_length=200,blank=True)



class VinBlanc(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origine_vin = models.CharField( max_length=200,blank=True)



class VinRosee(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField(default=0)
    origine_vin = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nom




