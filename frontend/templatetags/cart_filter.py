from cgitb import html
from itertools import product
from django import template
from store.models import ProductSize
from django.utils.safestring import mark_safe

register = template.Library()

def productSize_with_Qty(session_cart):

    carts = [
            {"product_size":ProductSize.objects.filter(id=key).first(),'qty':value} for key,value in session_cart.items() if ProductSize.objects.filter(id=key).first()
    ]
    return carts


@register.filter(name="get_carts")
def get_carts(session_cart):
    carts = productSize_with_Qty(session_cart)
    return carts

@register.filter(name="total_price")
def total_price(price,qty):
    return price*qty


@register.filter(name="total_amount")
def total_amount(session_cart):
    
    carts = productSize_with_Qty(session_cart)
    
    total = 0
    for cart in carts:
        total += cart['product_size'].product.price * cart['qty']
    return total


@register.filter(name="grand_total_amount")
def grand_total_amount(total_products_amount):
    tax = 0.13 * total_products_amount
    discount = 0.3 * total_products_amount
    delivery_charge = 100
    return total_products_amount+ tax - discount + delivery_charge

@register.filter(name="total_paid")
def total_paid(order):
    total_amount = 0
    for item in order.items.all():
        total_amount += item.product.product.price*item.qty
    
    return total_amount


    
@register.filter(name="order_status")
def order_status(order):
    status = order.get_status_display()
    
    if status == "approve":
        bc = "success"
    elif status=="cancel":
        bc = "danger"
    else:
        bc = "warning"

    return mark_safe(f'<span class="badge bg-{bc}">{status}</span>')