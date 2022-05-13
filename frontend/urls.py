import imp
from django.urls import path

from frontend.views.cart import cartView
from frontend.views.checkout import CheckoutView
from frontend.views.order import OrderView,cancelOrder
from .views.home import *
from .views.user_auth import *
from .views.products import *


urlpatterns = [
    path("",index,name="index"),
    path("user_login/",login_view,name="user_login"),
    path("user_register/",userRegisterView,name="user_register"),
    path("user_logout/",userLogout,name="user_logout"),
    path("products/",ProductView.as_view(),name="products"),
    path("products/<str:product_title>/",product_detail,name="product_detail"),
    path("product_size_stock/",product_size_stock,name="product_size_stock"),
    path("cart/",cartView,name="cart"),
    path("checkout/",CheckoutView.as_view(),name="checkout"),
    path("order/",OrderView.as_view(),name="order"),
    path("order_cancel/<str:order_id>/",cancelOrder,name="cancel_order"),
]
