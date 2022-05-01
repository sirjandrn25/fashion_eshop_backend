from django.urls import path
# from .views import index
from .views.user_auth import *

urlpatterns = [
    path("auth/user_login/",UserLoginApiView.as_view(),name="user_login"),
    path("auth/user_register/",UserRegisterApiView.as_view(),name="user_register"),
]


# urlpatterns = [
#     path("",index,name="home")
# ]
