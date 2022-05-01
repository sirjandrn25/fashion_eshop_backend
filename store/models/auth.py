from pyexpat import model
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from store.managers.auth_managers import UserManager




class User(AbstractBaseUser):
    email = models.EmailField(max_length=150,unique=True)
    contact_no = models.CharField(max_length=15,blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

class Profile(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "M", _("Male"),
        FEMALE = "F",_("Female"),
        OTHER = "O",_("Other")


    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100,blank=True)
    lastName = models.CharField(max_length=100,blank=True)
    gender = models.CharField(max_length=10,choices=GenderChoices.choices,default=GenderChoices.MALE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to="avatar/",blank=True,null=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}" if self.firstName and self.lastName else f"{self.user.email}"


class Address(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    provinance_no = models.CharField(max_length=5,default=1)
    city = models.CharField(max_length=150,blank=True)
    street = models.CharField(max_length=150,blank=True)
    zipcode = models.CharField(max_length=100,blank=True)

    # geo_lat = models.FloatField(null=True)
    # geo_long = models.FloatField(null=True)

    def __str__(self):
        return f"{self.city}" if self.city else f"{self.user.email}"

    
    