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


@register.filter(name="filter_category_fashion")
def filter_category_fashion(request,filter_name):
    fashion_value = request.GET.get('fashion')
    category_value = request.GET.get('category')
    if filter_name == 'fashion':
        return fashion_value if fashion_value else ""
    return category_value if category_value else ""

@register.filter(name="active_list_item_fashion")
def active_list_item_category(request,list_item):

    fashion_value = request.GET.get('fashion')
    if fashion_value is None:
        return ''
    return 'active bg-light' if list_item==fashion_value else ''

@register.filter(name="active_list_item_brand")
def active_list_item_brand(request,list_item):
    brand_value = request.GET.get('brand_value')
    if brand_value is None:
        return ''
    print(brand_value)
    return 'active bg-light' if list_item==brand_value else ''

            
    

