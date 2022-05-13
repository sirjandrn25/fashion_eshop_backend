from itertools import product
from venv import create
from django.db.models.signals import post_save
from django.dispatch import receiver
from store.models.product import *


@receiver(post_save,sender=Product)
def save_product_available(sender,**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    
    if created and instance.is_available:
        instance.is_available = False
        instance.save()
        

    else:
        if len(instance.sizes.all()) == 0 and instance.is_available:
            instance.is_available = False
            instance.save()

@receiver(post_save,sender=ProductSize)
def change_product_available(sender,**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    
    if created and instance.stock>0 and len(instance.product.sizes.all())==1 and not instance.product.is_available:
        print("change")
        instance.product.is_available = True
        instance.product.save()
    else:
        if instance.stock <1:
            product = instance.product
            flag = True
            for p_s in product.sizes.all():
                if p_s.stock >0:
                    flag = False
                    break
            if flag:
                product.is_available = False
                product.save()

                

        

    
            