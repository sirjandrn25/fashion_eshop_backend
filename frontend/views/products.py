
import imp
from django.views import View
from django.shortcuts import render,redirect
from store.models import Product,Fashion,Brand


class ProductView(View):
    def get(self,request):
        products = Product.objects.all()
        fashions = Fashion.objects.all()
        brands = Brand.objects.all()
        context = {
            'products':products,
            'fashions':fashions,
            'brands':brands
        }
        
        return render(request,"home/products.html",context)