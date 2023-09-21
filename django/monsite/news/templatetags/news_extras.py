#https://docs.djangoproject.com/fr/3.0/howto/custom-template-tags/
#Une fois les fichiers créés, il est nécessaire de spécifier une instance 
#de classe qui nous permettra d’enregistrer nos filtres et tags, de la même 
#manière que dans nos fichiers admin.py  avec admin.site.register(). 
#Pour ce faire, il faut déclarer les deux lignes suivantes au début du fichier blog_extras.py
from django import template
register = template.Library()
@register.filter
def citation(texte):   
    return "".format(texte)