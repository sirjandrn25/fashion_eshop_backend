from operator import mod
from django.db import models
from .product_utilities import *


class DateTimeTracker(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Product(DateTimeTracker):
    title = models.CharField(max_length=150,unique=True)
    price = models.FloatField()
    is_available = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="products")
    thumbnail = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.title


class ProductImages(DateTimeTracker):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/")
    def __str__(self):
        return self.product.title


class ProductSize(models.Model):
    size = models.CharField(max_length=150)
    stock = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='sizes')
    

    def __str__(self):
        return f"{self.size} >> {self.product.title}"
