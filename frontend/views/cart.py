from django.shortcuts import render,redirect





def cartView(request):
    
    if request.method == 'GET':
        
        product_size = request.GET.get('product_size')
        qty = request.GET.get('qty')
        if product_size and qty:
            carts = request.session.get('carts')
            if not carts:
                request.session['carts'] = {}
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
                
            except:
                print("error")
            return redirect("cart")
    
    return render(request,"home/cart.html")
    