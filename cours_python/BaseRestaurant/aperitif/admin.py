from django.contrib import admin
class Apéritifs(admin.ModelAdmin):
    list_display =('nom','prix','ingredient')
    search_fields = ['nom']



from .models import Tapa,Champagne,Cocktail,Classique,CocktailClassique,SansAlcools,Vodka,Gin, Whiskie
admin.site.register(Tapa)
admin.site.register(Champagne,Apéritifs)
admin.site.register(Cocktail,Apéritifs)
admin.site.register(Classique,Apéritifs)
admin.site.register(CocktailClassique,Apéritifs)
admin.site.register(SansAlcools,Apéritifs)
admin.site.register(Vodka,Apéritifs)
admin.site.register(Gin,Apéritifs)
admin.site.register(Whiskie,Apéritifs)





