from django import template

register = template.Library()


@register.filter(name="size_stock_range")
def size_stock_range(stock):
    
    qty_range = [qty+1 for qty in range(stock)]
    return qty_range

@register.filter(name="contain_cart_qty")
def contain_cart_qty(stock):
    if stock == 3:
        return "selected"
    return ''
