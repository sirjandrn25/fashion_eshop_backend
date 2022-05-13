from ast import Store
from django.views import View
from django.shortcuts import render,redirect
from store.models import *
from django.utils.decorators import method_decorator
from ..decorators import custom_login_required
from datetime import date

class OrderView(View):
    @method_decorator([custom_login_required("/user_login")])
    def get(self,request):
        order_status =  request.GET.get('order_status') if request.GET.get('order_status') else 'P'
        order_date = request.GET.get('order_date') if request.GET.get('order_date') else str(date.today())
        orders = Order.objects.filter(user=request.user,status=order_status,order_date=order_date)
        print(order_status)
        context = {
            'orders':orders,
            "order_date":order_date,
            "order_status":order_status

        }
        return render(request,"home/order.html",context)
    
    
        


def cancelOrder(request,order_id):
    order = Order.objects.filter(orderId=order_id).first()
    
    if order and order.user == request.user:
        order.status = "C"
        order.save()
        
    return redirect("order")

