
import imp
from django.views import View
from django.shortcuts import render,redirect
from store.models import Product,Fashion,Brand
from store.models.product_utilities import Category


class ProductView(View):
    def get(self,request):
        
        fashions = Fashion.objects.all()
        
        fashion = request.GET.get('fashion')
        category = request.GET.get('category')
        query = request.GET.get('query')
        brand = request.GET.get('brand')

       
        if fashion:
            
            fashion_obj = Fashion.objects.filter(fashion_name=fashion).first()

            if fashion_obj and category:
                category_obj = Category.objects.filter(fashion=fashion_obj,category_name=category).first()
                if category_obj:
                    products = list(Product.objects.filter(category=category_obj))
            else:
                products = []
                for category in fashion_obj.categories.all():
                    products.extend(list(Product.objects.filter(category=category)))

            brands = list(set(product.brand for product in products))
            
            
            if brand:
                brand_obj = Brand.objects.filter(brand_name=brand).first()
                if brand_obj:
                    products = [product for product in products if product.brand==brand_obj]
                    


        else:
            products = list(Product.objects.all())
            brands = Brand.objects.all()


        if query:
            products = [product for product in products if product.title.lower().startswith(query) ]



        context = {
            'products':products,
            'fashions':fashions,
            'brands':brands,
            'no_items':len(products)
        
        }
        
        return render(request,"home/products.html",context)