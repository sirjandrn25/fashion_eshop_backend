from itertools import product
from .product import *
from django.db import models
import uuid
from .auth import *
from django.utils.translation import gettext_lazy as _
import random
def randomOrderId():
    random_num = random.randrange(1000,20000)
    return str(random_num)



class Order(models.Model):
    class OrderStatusChoices(models.TextChoices):
        PENDING = 'P',_('pending')
        APPROVE = 'A',_('approve')
        CANCEL = 'C',_('cancel')
    
    class PaymentChoices(models.TextChoices):
        CASH = 'COD',_('Cash On Delivery')
        KHALTI = 'Khalti',_('Khalti')
        ESEWA =   'Esewa',_('E-Sewa')

    orderId = models.CharField(max_length=100,default=randomOrderId,unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    payment_way = models.CharField(max_length=15,choices=PaymentChoices.choices,default=PaymentChoices.CASH)
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(auto_now_add=True)
    valid_duration = models.IntegerField(default=15)
    status = models.CharField(max_length=15,choices=OrderStatusChoices.choices,default=OrderStatusChoices.PENDING)
    discount = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    address = models.ForeignKey('DeliveryAddress',on_delete=models.RESTRICT)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders")
    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.orderId}"

    class Meta:
        ordering = ['-id']

    
    @classmethod
    def save_cart_items(cls,obj,request):
        for key,value in request.session['carts'].items():
            product_size = ProductSize.objects.filter(id=key).first()
            if product_size:
                order_item = OrderItem(order=obj,product=product_size,qty=value,price=product_size.product.price)
                order_item.save()
        request.session['carts'] = {}



    

    


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(ProductSize,on_delete=models.CASCADE,related_name="orders")
    qty = models.IntegerField(default=1)
    price = models.FloatField()

    


class DeliveryAddress(models.Model):
    
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=150,blank=True,null=True)
    provinance_no = models.CharField(max_length=15)

    def __str__(self):
        return self.address


    




