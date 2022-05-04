import imp
from django.urls import path
from .views.home import *
from .views.user_auth import *


urlpatterns = [
    path("",index,name="index"),
    path("user_login/",login_view,name="user_login"),
    path("user_register/",userRegisterView,name="user_register"),
    path("user_logout/",userLogout,name="user_logout")
]
