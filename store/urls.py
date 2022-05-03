from django.urls import path,include
# from .views import index
from .views.user_auth import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserAPIView, basename='user')



urlpatterns = [
    path("",include(router.urls)),
    path("auth/user_login/",UserLoginApiView.as_view()),
    path("auth/user_register/",UserRegisterApiView.as_view()),
]


# urlpatterns = [
#     path("",index,name="home")
# ]
