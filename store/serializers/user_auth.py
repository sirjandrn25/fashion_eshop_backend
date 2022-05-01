from rest_framework.serializers import Serializer
from rest_framework import serializers
from store.models.auth import User
from django.contrib.auth.hashers import check_password,make_password

class UserLoginSerializer(Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self,validated_data):
        email = validated_data.get('email','')
        password = validated_data.get('password','')

        if email and password:
            user = User.objects.filter(email=email).first()
            if user:
                if check_password(password,user.password):
                    validated_data['user'] = user
                    return validated_data
                else:
                    errors = {
                        'password':["incorrect password !!!"]
                    }
            else:
                errors = {
                    'email':["this email id does not exist"]
                }
        else:
            errors = {
                "password":["this field may be required"],
                "email":["this field may be required"],
            }
        raise serializers.ValidationError(errors)

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ['id']
    
    def validate(self,validated_data):
        password = validated_data.get('password')

        if len(password) <8:
            errors = {
                'password':['at least 8 charecters are required']
            }
        elif password.isdigit():
            errors = {
                'password':['only numeric values are not allowed']
            }
        else:
            validated_data['password'] = make_password(password)
            return validated_data
        raise serializers.ValidationError(errors)
    