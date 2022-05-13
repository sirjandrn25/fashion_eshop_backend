from django.db.models.signals import post_save
from django.dispatch import receiver
from store.models.order import *
from store.models.product import *

@receiver(post_save,sender=Order)
def change_product_stock(sender,**kwarg):
    created = kwarg.get('created')
    print("order changes")
    instance = kwarg.get('instance')

    if not created and instance.get_status_display()=="approve":
        for order_item in instance.items.all():
            product_size = order_item.product
            product_size.stock = product_size.stock - order_item.qty
            product_size.save()
    

        