from django.contrib import admin
from backoffice.models import *

class ProductItemAdmin(admin.TabularInline):
    model = ProductItem

class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ProductItemAdmin,]

admin.site.register(Product, ProductAdmin)

class ProductFilter(admin.SimpleListFilter):
   
    title = 'filtre produit'
    parameter_name = 'custom_status'

    def lookups(self, request, model_admin):
        return (
            ('online', 'En ligne'),
            ('offline', 'Hors ligne'),
        )

    def queryset(self, request, queryset):
 
        if self.value() == 'online':
            return queryset.filter(status=1)
                                    
        if self.value() == 'offline':
            return queryset.filter(status=0)

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id', 'name', 'date_creation', 'status')
    list_filter = (ProductFilter,)

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id', 'name', 'date_creation', 'status')
    date_hierarchy = 'date_creation'

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id', 'name', 'date_creation', 'status')
    ordering = ('-date_creation',)

	
def set_product_online(modeladmin, request, queryset):
    queryset.update(status=1)
set_product_online.short_description = "Mettre en ligne"

class ProductAdmin(admin.ModelAdmin):
    model = Product
    actions = [set_product_online]

class ProductAdmin(admin.ModelAdmin):
    model = Product
    
    list_display = ('id', 'name', 'date_creation', 'status', 'tax')
    
    def tax(self, instance):
        return instance.price_ttc - instance.price_ht
    tax.short_description = "Taxes"

	
	
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("code", "name", "items_code")
     
    def items_code(self, instance):
        string = ""
        for product_item in instance.product_item.all():
            string+=product_item.code
        return string
    items_code.admin_order_field = 'product_item'

    
    def queryset(self, request):
        qs = super(ProductAdmin, self).queryset(request)
        qs = qs.prefetch_related("product_item")
        return qs

		
		
		
from django.db.models import Count

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("code", "name", "product_item_count")
    
    def product_item_count(self, obj):
      return obj.product_item_count
    
    def queryset(self, request):
        qs = super(ProductAdmin, self).queryset(request)
        return qs.annotate(product_item_count=Count('product_item'))

		
		
