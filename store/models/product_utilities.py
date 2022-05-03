import imp
from pyexpat import model
from statistics import mode
from unicodedata import category
from django.db import models



class Fashion(models.Model):
    fashion_name = models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.fashion_name



class Category(models.Model):
    category_name = models.CharField(max_length=120)
    fashion = models.OneToOneField(Fashion,on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name



class Brand(models.Model):
    brand_name = models.CharField(max_length=150,unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name
    