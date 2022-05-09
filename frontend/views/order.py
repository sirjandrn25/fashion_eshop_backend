from ast import Store
from django.views import View
from django.shortcuts import render
from store.models import *
from django.utils.decorators import method_decorator
from ..decorators import custom_login_required

class OrderView(View):
    @method_decorator([custom_login_required("/user_login")])
    def get(self,request):
        
        orders = Order.objects.filter(user=request.user)
        context = {
            'orders':orders
        }
        return render(request,"home/order.html",context)