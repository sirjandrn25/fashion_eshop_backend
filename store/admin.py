from django.contrib import admin
from store.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Fashion)
admin.site.register(Brand)
# admin.site.register(ProductSize)


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['id','size','product_name']

    @admin.display(description="product_name")
    def product_name(self,obj):
        return obj.product.title