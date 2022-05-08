

from django.shortcuts import render,redirect
from frontend.decorators import custom_login_required,IsAnyItemInCart
from frontend.forms.checkout import CheckoutForm
from django.views import View
from django.utils.decorators import method_decorator
from store.models.order import *



class CheckoutView(View):
    
    @method_decorator([custom_login_required("/user_login"),IsAnyItemInCart])
    def get(self,request):
        order = Order.objects.filter(user=request.user).last()

        if order:
        
            form = CheckoutForm(data=(order.__dict__|order.address.__dict__))
            request.session['prev_order_address'] = order.address.id
        else:
            form = CheckoutForm()
            request.session['prev_order_address'] = False
            
            
        context = {
            'form':form
        }

        return render(request,"home/checkout.html",context)
    
    @method_decorator(custom_login_required("/user_login"))
    def post(self,request):
        form = CheckoutForm(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            contact_no = form.cleaned_data['contact_no']
            payment_way = form.cleaned_data['payment_way']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            
            provinance_no = form.cleaned_data['provinance_no']
            street = form.cleaned_data['street']
            zip_code = form.cleaned_data['zip_code']
        
            save_delivery_address = form.cleaned_data['save_delivery_address']
            
            if save_delivery_address or not request.session['prev_order_address']:
                delivery_address = DeliveryAddress(address=address,provinance_no=provinance_no,zip_code=zip_code,street=street,city=city)
                delivery_address.save()
            else:
                try:
                    delivery_address = DeliveryAddress.objects.get(id=request.session['prev_order_address'])
                except Exception as e:
                    print(e)
            
            order = Order(firstName=firstName,lastName=lastName,contact_no=contact_no,payment_way=payment_way,user=request.user,address=delivery_address)

            order.save()
            Order.save_cart_items(order,request)
            return redirect('order')
            # print(firstName,lastName,city,contact_no,payment_way,address,street,provinance_no,zip_code,save_delivery_address)

            


            
        return render(request,"home/checkout.html",context)
    
    



    