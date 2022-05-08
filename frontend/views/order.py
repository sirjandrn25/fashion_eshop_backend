from ast import Store
from django.views import View
from django.shortcuts import render
from store.models import *



class OrderView(View):
    def get(self,request):
        
        orders = Order.objects.filter(user=request.user)
        context = {
            'orders':orders
        }
        return render(request,"home/order.html",context)