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


def product_detail(request,product_title):

    product = Product.objects.filter(title=product_title).first()

    # get in stock sizes 
    sizes = [size for size in ProductSize.objects.filter(product=product) if size.stock>0]
    context = {
        'product':product,
        'sizes':sizes
    }
    
    return render(request,"home/product_detail.html",context)



# def get_product_size_stocks(request):
#     if request.method == 'GET':
#         product_size = request.GET['product_size']
#         product = request.GET['product']

