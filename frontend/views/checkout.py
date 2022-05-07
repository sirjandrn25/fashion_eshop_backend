import imp
from django.shortcuts import render
from frontend.decorators import custom_login_required
from frontend.forms.checkout import CheckoutForm
from django.views import View
from django.utils.decorators import method_decorator



class CheckoutView(View):
    @method_decorator(custom_login_required('/user_login'))
    def get(self,request):
        form = CheckoutForm()
        context = {
            'form':form
        }

        return render(request,"home/checkout.html",context)
    
    @method_decorator(custom_login_required('/user_login'))
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
            print(firstName,lastName,city,contact_no,payment_way,address,street,provinance_no,zip_code,save_delivery_address)
            


            
        return render(request,"home/checkout.html",context)
    
    



    