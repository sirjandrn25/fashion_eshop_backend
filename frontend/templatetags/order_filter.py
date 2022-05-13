from urllib import request
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


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

@register.filter(name="select_order_status")
def select_order_status(request,status_label):
    order_status = request.GET.get('order_status')
    if order_status and status_label == order_status:
        return "selected"
    return ''
            

@register.filter(name="check_cancel_order")
def check_cancel_order(order):
    
    if order.get_status_display() == "pending":
        return True
    return False