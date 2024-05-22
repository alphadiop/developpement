from django.contrib import admin

class BaseRestaurantAdmin(admin.ModelAdmin):
    list_display = ('nom','prix','origin_viande','commentaire')
    search_fields = ['nom']
class EnfantAdmin(admin.ModelAdmin):
    list_display = ('nom_et_ou_prix','commentaire')
    search_fields = ['nom']


from .models import Entree
from .models import Plat
from .models import Suggestion_Plat
from .models import Dessert
from .models import PrixMenuEnfant
from .models import PlatMenuEnfant
from .models import DessertEnfant
admin.site.register(Entree,BaseRestaurantAdmin)
admin.site.register(Plat,BaseRestaurantAdmin)
admin.site.register(Suggestion_Plat,BaseRestaurantAdmin)
admin.site.register(Dessert,BaseRestaurantAdmin)
admin.site.register(PrixMenuEnfant,EnfantAdmin)
admin.site.register(PlatMenuEnfant,EnfantAdmin)
admin.site.register(DessertEnfant,EnfantAdmin)


