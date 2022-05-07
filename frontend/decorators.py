from email import message
from django.shortcuts import redirect
from django.contrib import messages

def custom_login_required(login_url="/user_login"):
    
    
    def wrapper(func):
        def inner(request,*args,**kwargs):
            
            if request.user.is_authenticated:
                return func(request,*args,**kwargs)
            print(request.META.get('HTTP_REFERER'))
            request.session['after_login_url'] = request.path_info
            messages.error(request,"please login first required")
            return redirect(login_url)
        return inner
    return wrapper

def IsAnyItemInCart(func):
    def inner(request,*args,**kwargs):
        try:
            carts = request.session['carts']
        except:
            carts = {}
        if len(carts.keys())>0:
            return func(request,*args,**kwargs)
        
        messages.error(request,"first some items add in cart")
        return redirect("cart")
    return inner

