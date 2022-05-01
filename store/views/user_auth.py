import imp
from rest_framework import generics
from store.serializers.user_auth import UserLoginSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from store.models.auth import User

class UserLoginApiView(generics.GenericAPIView):
    # serializer = UserLoginSerializer
    def post(self,request):
        
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            resp = {
                'access':'46689'
            }
            return Response(resp)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class UserRegisterApiView(generics.GenericAPIView):
    # serializer = UserSerializer

    def post(self,request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response()
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class UserAPIViewsets(viewsets.ModelViewSet):
#     serializer = UserSerializer
#     queryset = User.objects.all()

