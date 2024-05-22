from django.db import models

class CommonInfo(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField(default=0)
    ingredient = models.CharField(max_length=200, blank=True)

    class Meta:
        abstract = True
    def __str__(self):
        return self.nom


class Tapa(CommonInfo):
    pass
class Champagne(CommonInfo):
    pass
class Cocktail (CommonInfo):
    pass
class Classique(CommonInfo):
    pass
class CocktailClassique(CommonInfo):
    pass
class SansAlcools(CommonInfo):
    pass
class Vodka(CommonInfo):
    pass
class Gin (CommonInfo):
    pass
class Whiskie(CommonInfo):
    pass



