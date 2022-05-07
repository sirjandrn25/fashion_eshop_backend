from django.shortcuts import render,redirect
from frontend.decorators import custom_login_required



def cartView(request):
    carts = request.session.get('carts') 
    print(request.session.keys())
    if not carts:
        request.session['carts'] = {}
        carts = {}
    
    if request.method == 'GET':
        
        product_size = request.GET.get('product_size')
        qty = request.GET.get('qty')
        if product_size and qty:
            
            try:
                qty = int(qty)
                if qty>0:
                    carts[product_size] = qty
                else:
                    # remove the product from cart if product qty = 0
                    product_size_present = True if product_size in carts.keys() else False
                    if product_size_present:
                        carts.pop(product_size)
                    
                request.session['carts'] = carts
                
            except Exception as e:
                print(e)
                
            return redirect("cart")
    
    return render(request,"home/cart.html")
    