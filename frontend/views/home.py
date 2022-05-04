from django.shortcuts import render
from store.models.product import *
from store.models.product_utilities import *

# Create your views here.

def index(request):
    
    fashions = Fashion.objects.all()
    products = Product.objects.all()

    context = {
        'fashions':fashions,
        'products':products
    }

    return render(request,"home/index.html",context)



